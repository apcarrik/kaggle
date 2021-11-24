def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Gender, obj[4]: Age, obj[5]: Children, obj[6]: Education, obj[7]: Occupation, obj[8]: Income, obj[9]: Bar, obj[10]: Coffeehouse, obj[11]: Restaurant20to50, obj[12]: Direction_same, obj[13]: Distance
	# {"feature": "Income", "instances": 23, "metric_value": 0.8281, "depth": 1}
	if obj[8]<=4:
		# {"feature": "Coffeehouse", "instances": 12, "metric_value": 1.0, "depth": 2}
		if obj[10]<=2.0:
			# {"feature": "Coupon", "instances": 9, "metric_value": 0.9183, "depth": 3}
			if obj[2]<=3:
				return 'True'
			elif obj[2]>3:
				# {"feature": "Age", "instances": 4, "metric_value": 0.8113, "depth": 4}
				if obj[4]<=4:
					return 'False'
				elif obj[4]>4:
					return 'True'
				else: return 'True'
			else: return 'False'
		elif obj[10]>2.0:
			return 'False'
		else: return 'False'
	elif obj[8]>4:
		return 'True'
	else: return 'True'
