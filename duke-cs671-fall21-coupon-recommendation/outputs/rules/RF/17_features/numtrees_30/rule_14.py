def findDecision(obj): #obj[0]: Passanger, obj[1]: Weather, obj[2]: Time, obj[3]: Coupon, obj[4]: Coupon_validity, obj[5]: Gender, obj[6]: Age, obj[7]: Maritalstatus, obj[8]: Children, obj[9]: Education, obj[10]: Occupation, obj[11]: Income, obj[12]: Bar, obj[13]: Coffeehouse, obj[14]: Restaurant20to50, obj[15]: Direction_same, obj[16]: Distance
	# {"feature": "Coupon", "instances": 34, "metric_value": 0.9774, "depth": 1}
	if obj[3]<=3:
		# {"feature": "Children", "instances": 21, "metric_value": 0.7919, "depth": 2}
		if obj[8]>0:
			# {"feature": "Restaurant20to50", "instances": 11, "metric_value": 0.994, "depth": 3}
			if obj[14]<=1.0:
				# {"feature": "Time", "instances": 6, "metric_value": 0.65, "depth": 4}
				if obj[2]<=3:
					return 'True'
				elif obj[2]>3:
					return 'False'
				else: return 'False'
			elif obj[14]>1.0:
				# {"feature": "Time", "instances": 5, "metric_value": 0.7219, "depth": 4}
				if obj[2]<=1:
					return 'False'
				elif obj[2]>1:
					# {"feature": "Passanger", "instances": 2, "metric_value": 1.0, "depth": 5}
					if obj[0]<=1:
						return 'False'
					elif obj[0]>1:
						return 'True'
					else: return 'True'
				else: return 'False'
			else: return 'False'
		elif obj[8]<=0:
			return 'True'
		else: return 'True'
	elif obj[3]>3:
		# {"feature": "Gender", "instances": 13, "metric_value": 0.8905, "depth": 2}
		if obj[5]>0:
			# {"feature": "Occupation", "instances": 7, "metric_value": 0.9852, "depth": 3}
			if obj[10]<=10:
				return 'True'
			elif obj[10]>10:
				return 'False'
			else: return 'False'
		elif obj[5]<=0:
			return 'False'
		else: return 'False'
	else: return 'False'
