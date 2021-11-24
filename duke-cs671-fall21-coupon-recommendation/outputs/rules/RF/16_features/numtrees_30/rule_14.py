def findDecision(obj): #obj[0]: Passanger, obj[1]: Weather, obj[2]: Time, obj[3]: Coupon, obj[4]: Coupon_validity, obj[5]: Gender, obj[6]: Age, obj[7]: Children, obj[8]: Education, obj[9]: Occupation, obj[10]: Income, obj[11]: Bar, obj[12]: Coffeehouse, obj[13]: Restaurant20to50, obj[14]: Direction_same, obj[15]: Distance
	# {"feature": "Passanger", "instances": 34, "metric_value": 0.9367, "depth": 1}
	if obj[0]<=2:
		# {"feature": "Time", "instances": 19, "metric_value": 0.9495, "depth": 2}
		if obj[2]<=1:
			# {"feature": "Income", "instances": 10, "metric_value": 0.971, "depth": 3}
			if obj[10]<=4:
				# {"feature": "Bar", "instances": 6, "metric_value": 0.9183, "depth": 4}
				if obj[11]<=2.0:
					return 'False'
				elif obj[11]>2.0:
					return 'True'
				else: return 'True'
			elif obj[10]>4:
				return 'True'
			else: return 'True'
		elif obj[2]>1:
			# {"feature": "Education", "instances": 9, "metric_value": 0.5033, "depth": 3}
			if obj[8]<=3:
				return 'False'
			elif obj[8]>3:
				# {"feature": "Coupon", "instances": 2, "metric_value": 1.0, "depth": 4}
				if obj[3]>1:
					return 'False'
				elif obj[3]<=1:
					return 'True'
				else: return 'True'
			else: return 'False'
		else: return 'False'
	elif obj[0]>2:
		return 'True'
	else: return 'True'
