def findDecision(obj): #obj[0]: Passanger, obj[1]: Weather, obj[2]: Time, obj[3]: Coupon, obj[4]: Coupon_validity, obj[5]: Gender, obj[6]: Age, obj[7]: Maritalstatus, obj[8]: Children, obj[9]: Education, obj[10]: Occupation, obj[11]: Income, obj[12]: Bar, obj[13]: Coffeehouse, obj[14]: Restaurant20to50, obj[15]: Direction_same, obj[16]: Distance
	# {"feature": "Coupon_validity", "instances": 23, "metric_value": 0.8281, "depth": 1}
	if obj[4]<=0:
		# {"feature": "Age", "instances": 15, "metric_value": 0.971, "depth": 2}
		if obj[6]<=3:
			# {"feature": "Income", "instances": 10, "metric_value": 0.971, "depth": 3}
			if obj[11]>4:
				# {"feature": "Education", "instances": 6, "metric_value": 0.65, "depth": 4}
				if obj[9]>0:
					return 'False'
				elif obj[9]<=0:
					return 'True'
				else: return 'True'
			elif obj[11]<=4:
				# {"feature": "Time", "instances": 4, "metric_value": 0.8113, "depth": 4}
				if obj[2]<=2:
					return 'True'
				elif obj[2]>2:
					return 'False'
				else: return 'False'
			else: return 'True'
		elif obj[6]>3:
			return 'True'
		else: return 'True'
	elif obj[4]>0:
		return 'True'
	else: return 'True'
