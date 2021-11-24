def findDecision(obj): #obj[0]: Passanger, obj[1]: Weather, obj[2]: Time, obj[3]: Coupon, obj[4]: Coupon_validity, obj[5]: Gender, obj[6]: Age, obj[7]: Maritalstatus, obj[8]: Children, obj[9]: Education, obj[10]: Occupation, obj[11]: Income, obj[12]: Bar, obj[13]: Coffeehouse, obj[14]: Restaurant20to50, obj[15]: Direction_same, obj[16]: Distance
	# {"feature": "Maritalstatus", "instances": 23, "metric_value": 0.9656, "depth": 1}
	if obj[7]<=1:
		# {"feature": "Coffeehouse", "instances": 18, "metric_value": 0.8524, "depth": 2}
		if obj[13]<=1.0:
			# {"feature": "Weather", "instances": 11, "metric_value": 0.994, "depth": 3}
			if obj[1]<=0:
				# {"feature": "Age", "instances": 8, "metric_value": 0.9544, "depth": 4}
				if obj[6]<=2:
					# {"feature": "Occupation", "instances": 5, "metric_value": 0.971, "depth": 5}
					if obj[10]<=11:
						return 'False'
					elif obj[10]>11:
						return 'True'
					else: return 'True'
				elif obj[6]>2:
					return 'True'
				else: return 'True'
			elif obj[1]>0:
				return 'False'
			else: return 'False'
		elif obj[13]>1.0:
			return 'False'
		else: return 'False'
	elif obj[7]>1:
		# {"feature": "Occupation", "instances": 5, "metric_value": 0.7219, "depth": 2}
		if obj[10]<=10:
			return 'True'
		elif obj[10]>10:
			return 'False'
		else: return 'False'
	else: return 'True'
