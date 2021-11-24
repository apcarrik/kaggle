def findDecision(obj): #obj[0]: Passanger, obj[1]: Weather, obj[2]: Time, obj[3]: Coupon, obj[4]: Coupon_validity, obj[5]: Gender, obj[6]: Age, obj[7]: Maritalstatus, obj[8]: Children, obj[9]: Education, obj[10]: Occupation, obj[11]: Income, obj[12]: Bar, obj[13]: Coffeehouse, obj[14]: Restaurant20to50, obj[15]: Direction_same, obj[16]: Distance
	# {"feature": "Coupon_validity", "instances": 34, "metric_value": 0.99, "depth": 1}
	if obj[4]<=0:
		# {"feature": "Occupation", "instances": 21, "metric_value": 0.9587, "depth": 2}
		if obj[10]<=14:
			# {"feature": "Coupon", "instances": 18, "metric_value": 0.8524, "depth": 3}
			if obj[3]>2:
				return 'True'
			elif obj[3]<=2:
				# {"feature": "Gender", "instances": 8, "metric_value": 0.9544, "depth": 4}
				if obj[5]<=0:
					return 'False'
				elif obj[5]>0:
					# {"feature": "Maritalstatus", "instances": 4, "metric_value": 0.8113, "depth": 5}
					if obj[7]<=1:
						return 'True'
					elif obj[7]>1:
						return 'False'
					else: return 'False'
				else: return 'True'
			else: return 'False'
		elif obj[10]>14:
			return 'False'
		else: return 'False'
	elif obj[4]>0:
		# {"feature": "Occupation", "instances": 13, "metric_value": 0.6194, "depth": 2}
		if obj[10]<=10:
			return 'False'
		elif obj[10]>10:
			# {"feature": "Weather", "instances": 4, "metric_value": 1.0, "depth": 3}
			if obj[1]<=0:
				# {"feature": "Passanger", "instances": 3, "metric_value": 0.9183, "depth": 4}
				if obj[0]>1:
					# {"feature": "Age", "instances": 2, "metric_value": 1.0, "depth": 5}
					if obj[6]<=1:
						return 'True'
					elif obj[6]>1:
						return 'False'
					else: return 'False'
				elif obj[0]<=1:
					return 'False'
				else: return 'False'
			elif obj[1]>0:
				return 'True'
			else: return 'True'
		else: return 'False'
	else: return 'False'
