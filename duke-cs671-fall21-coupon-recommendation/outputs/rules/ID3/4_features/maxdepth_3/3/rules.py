def findDecision(obj): #obj[0]: Coupon, obj[1]: Education, obj[2]: Occupation, obj[3]: Distance
	# {"feature": "Coupon", "instances": 8147, "metric_value": 0.4716, "depth": 1}
	if obj[0]>1:
		# {"feature": "Distance", "instances": 5887, "metric_value": 0.4585, "depth": 2}
		if obj[3]<=2:
			# {"feature": "Occupation", "instances": 5324, "metric_value": 0.4541, "depth": 3}
			if obj[2]>0:
				# {"feature": "Education", "instances": 5265, "metric_value": 0.4556, "depth": 4}
				if obj[1]<=4:
					return 'True'
				elif obj[1]>4:
					return 'True'
				else: return 'True'
			elif obj[2]<=0:
				# {"feature": "Education", "instances": 59, "metric_value": 0.3021, "depth": 4}
				if obj[1]<=0:
					return 'True'
				elif obj[1]>0:
					return 'True'
				else: return 'True'
			else: return 'True'
		elif obj[3]>2:
			# {"feature": "Education", "instances": 563, "metric_value": 0.4901, "depth": 3}
			if obj[1]<=3:
				# {"feature": "Occupation", "instances": 513, "metric_value": 0.4884, "depth": 4}
				if obj[2]<=7.83625730994152:
					return 'False'
				elif obj[2]>7.83625730994152:
					return 'False'
				else: return 'False'
			elif obj[1]>3:
				# {"feature": "Occupation", "instances": 50, "metric_value": 0.463, "depth": 4}
				if obj[2]<=11:
					return 'True'
				elif obj[2]>11:
					return 'True'
				else: return 'True'
			else: return 'True'
		else: return 'False'
	elif obj[0]<=1:
		# {"feature": "Occupation", "instances": 2260, "metric_value": 0.4819, "depth": 2}
		if obj[2]>2.0261754612655967:
			# {"feature": "Education", "instances": 1792, "metric_value": 0.4903, "depth": 3}
			if obj[1]>0:
				# {"feature": "Distance", "instances": 1168, "metric_value": 0.483, "depth": 4}
				if obj[3]<=2:
					return 'False'
				elif obj[3]>2:
					return 'False'
				else: return 'False'
			elif obj[1]<=0:
				# {"feature": "Distance", "instances": 624, "metric_value": 0.4998, "depth": 4}
				if obj[3]>1:
					return 'False'
				elif obj[3]<=1:
					return 'True'
				else: return 'True'
			else: return 'True'
		elif obj[2]<=2.0261754612655967:
			# {"feature": "Education", "instances": 468, "metric_value": 0.4172, "depth": 3}
			if obj[1]<=3:
				# {"feature": "Distance", "instances": 417, "metric_value": 0.4077, "depth": 4}
				if obj[3]<=2:
					return 'False'
				elif obj[3]>2:
					return 'False'
				else: return 'False'
			elif obj[1]>3:
				# {"feature": "Distance", "instances": 51, "metric_value": 0.457, "depth": 4}
				if obj[3]<=2:
					return 'True'
				elif obj[3]>2:
					return 'True'
				else: return 'True'
			else: return 'True'
		else: return 'False'
	else: return 'False'
