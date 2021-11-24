def findDecision(obj): #obj[0]: Coupon, obj[1]: Education, obj[2]: Occupation, obj[3]: Restaurant20to50, obj[4]: Distance
	# {"feature": "Distance", "instances": 51, "metric_value": 0.9183, "depth": 1}
	if obj[4]>1:
		# {"feature": "Occupation", "instances": 33, "metric_value": 0.994, "depth": 2}
		if obj[2]<=11:
			# {"feature": "Education", "instances": 23, "metric_value": 0.9656, "depth": 3}
			if obj[1]<=3:
				# {"feature": "Coupon", "instances": 22, "metric_value": 0.9457, "depth": 4}
				if obj[0]>0:
					# {"feature": "Restaurant20to50", "instances": 17, "metric_value": 0.9774, "depth": 5}
					if obj[3]>0.0:
						return 'False'
					elif obj[3]<=0.0:
						return 'False'
					else: return 'False'
				elif obj[0]<=0:
					# {"feature": "Restaurant20to50", "instances": 5, "metric_value": 0.7219, "depth": 5}
					if obj[3]>0.0:
						return 'False'
					elif obj[3]<=0.0:
						return 'True'
					else: return 'True'
				else: return 'False'
			elif obj[1]>3:
				return 'True'
			else: return 'True'
		elif obj[2]>11:
			# {"feature": "Education", "instances": 10, "metric_value": 0.469, "depth": 3}
			if obj[1]>0:
				return 'True'
			elif obj[1]<=0:
				# {"feature": "Coupon", "instances": 2, "metric_value": 1.0, "depth": 4}
				if obj[0]<=0:
					return 'False'
				elif obj[0]>0:
					return 'True'
				else: return 'True'
			else: return 'False'
		else: return 'True'
	elif obj[4]<=1:
		# {"feature": "Coupon", "instances": 18, "metric_value": 0.5033, "depth": 2}
		if obj[0]>0:
			# {"feature": "Restaurant20to50", "instances": 17, "metric_value": 0.3228, "depth": 3}
			if obj[3]>0.0:
				return 'True'
			elif obj[3]<=0.0:
				return 'False'
			else: return 'False'
		elif obj[0]<=0:
			return 'False'
		else: return 'False'
	else: return 'True'
