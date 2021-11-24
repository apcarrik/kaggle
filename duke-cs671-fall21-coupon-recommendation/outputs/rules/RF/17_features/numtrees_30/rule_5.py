def findDecision(obj): #obj[0]: Passanger, obj[1]: Weather, obj[2]: Time, obj[3]: Coupon, obj[4]: Coupon_validity, obj[5]: Gender, obj[6]: Age, obj[7]: Maritalstatus, obj[8]: Children, obj[9]: Education, obj[10]: Occupation, obj[11]: Income, obj[12]: Bar, obj[13]: Coffeehouse, obj[14]: Restaurant20to50, obj[15]: Direction_same, obj[16]: Distance
	# {"feature": "Coffeehouse", "instances": 34, "metric_value": 0.9975, "depth": 1}
	if obj[13]<=1.0:
		# {"feature": "Coupon", "instances": 21, "metric_value": 0.8631, "depth": 2}
		if obj[3]>0:
			# {"feature": "Time", "instances": 16, "metric_value": 0.9544, "depth": 3}
			if obj[2]>2:
				# {"feature": "Gender", "instances": 8, "metric_value": 0.9544, "depth": 4}
				if obj[5]<=0:
					# {"feature": "Passanger", "instances": 5, "metric_value": 0.971, "depth": 5}
					if obj[0]<=1:
						return 'False'
					elif obj[0]>1:
						return 'True'
					else: return 'True'
				elif obj[5]>0:
					return 'True'
				else: return 'True'
			elif obj[2]<=2:
				# {"feature": "Direction_same", "instances": 8, "metric_value": 0.5436, "depth": 4}
				if obj[15]<=0:
					return 'False'
				elif obj[15]>0:
					return 'True'
				else: return 'True'
			else: return 'False'
		elif obj[3]<=0:
			return 'False'
		else: return 'False'
	elif obj[13]>1.0:
		# {"feature": "Bar", "instances": 13, "metric_value": 0.7793, "depth": 2}
		if obj[12]<=3.0:
			# {"feature": "Age", "instances": 11, "metric_value": 0.4395, "depth": 3}
			if obj[6]<=6:
				return 'True'
			elif obj[6]>6:
				return 'False'
			else: return 'False'
		elif obj[12]>3.0:
			return 'False'
		else: return 'False'
	else: return 'True'
