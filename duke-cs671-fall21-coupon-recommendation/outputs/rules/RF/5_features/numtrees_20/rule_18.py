def findDecision(obj): #obj[0]: Coupon, obj[1]: Education, obj[2]: Occupation, obj[3]: Restaurant20to50, obj[4]: Distance
	# {"feature": "Education", "instances": 51, "metric_value": 0.8974, "depth": 1}
	if obj[1]>1:
		# {"feature": "Occupation", "instances": 31, "metric_value": 0.9812, "depth": 2}
		if obj[2]<=13:
			# {"feature": "Restaurant20to50", "instances": 29, "metric_value": 0.9576, "depth": 3}
			if obj[3]>0.0:
				# {"feature": "Distance", "instances": 25, "metric_value": 0.9044, "depth": 4}
				if obj[4]<=1:
					# {"feature": "Coupon", "instances": 15, "metric_value": 0.9968, "depth": 5}
					if obj[0]>0:
						return 'True'
					elif obj[0]<=0:
						return 'False'
					else: return 'False'
				elif obj[4]>1:
					# {"feature": "Coupon", "instances": 10, "metric_value": 0.469, "depth": 5}
					if obj[0]>1:
						return 'True'
					elif obj[0]<=1:
						return 'False'
					else: return 'False'
				else: return 'True'
			elif obj[3]<=0.0:
				# {"feature": "Coupon", "instances": 4, "metric_value": 0.8113, "depth": 4}
				if obj[0]>0:
					return 'False'
				elif obj[0]<=0:
					return 'True'
				else: return 'True'
			else: return 'False'
		elif obj[2]>13:
			return 'False'
		else: return 'False'
	elif obj[1]<=1:
		# {"feature": "Occupation", "instances": 20, "metric_value": 0.6098, "depth": 2}
		if obj[2]>0:
			# {"feature": "Coupon", "instances": 19, "metric_value": 0.4855, "depth": 3}
			if obj[0]>0:
				# {"feature": "Distance", "instances": 17, "metric_value": 0.3228, "depth": 4}
				if obj[4]>1:
					return 'True'
				elif obj[4]<=1:
					# {"feature": "Restaurant20to50", "instances": 6, "metric_value": 0.65, "depth": 5}
					if obj[3]<=1.0:
						return 'True'
					elif obj[3]>1.0:
						return 'True'
					else: return 'True'
				else: return 'True'
			elif obj[0]<=0:
				# {"feature": "Restaurant20to50", "instances": 2, "metric_value": 1.0, "depth": 4}
				if obj[3]>1.0:
					return 'False'
				elif obj[3]<=1.0:
					return 'True'
				else: return 'True'
			else: return 'False'
		elif obj[2]<=0:
			return 'False'
		else: return 'False'
	else: return 'True'
