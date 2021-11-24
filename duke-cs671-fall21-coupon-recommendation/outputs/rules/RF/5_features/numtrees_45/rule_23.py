def findDecision(obj): #obj[0]: Coupon, obj[1]: Education, obj[2]: Occupation, obj[3]: Restaurant20to50, obj[4]: Distance
	# {"feature": "Restaurant20to50", "instances": 23, "metric_value": 0.9321, "depth": 1}
	if obj[3]<=1.0:
		# {"feature": "Occupation", "instances": 14, "metric_value": 1.0, "depth": 2}
		if obj[2]<=10:
			# {"feature": "Coupon", "instances": 11, "metric_value": 0.9457, "depth": 3}
			if obj[0]>3:
				# {"feature": "Education", "instances": 6, "metric_value": 0.9183, "depth": 4}
				if obj[1]>0:
					# {"feature": "Distance", "instances": 5, "metric_value": 0.7219, "depth": 5}
					if obj[4]<=1:
						return 'False'
					elif obj[4]>1:
						return 'False'
					else: return 'False'
				elif obj[1]<=0:
					return 'True'
				else: return 'True'
			elif obj[0]<=3:
				return 'True'
			else: return 'True'
		elif obj[2]>10:
			return 'False'
		else: return 'False'
	elif obj[3]>1.0:
		# {"feature": "Education", "instances": 9, "metric_value": 0.5033, "depth": 2}
		if obj[1]<=2:
			return 'True'
		elif obj[1]>2:
			# {"feature": "Occupation", "instances": 4, "metric_value": 0.8113, "depth": 3}
			if obj[2]>6:
				# {"feature": "Distance", "instances": 2, "metric_value": 1.0, "depth": 4}
				if obj[4]>1:
					return 'False'
				elif obj[4]<=1:
					return 'True'
				else: return 'True'
			elif obj[2]<=6:
				return 'True'
			else: return 'True'
		else: return 'True'
	else: return 'True'
