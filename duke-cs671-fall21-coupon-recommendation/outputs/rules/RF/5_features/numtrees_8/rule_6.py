def findDecision(obj): #obj[0]: Coupon, obj[1]: Education, obj[2]: Occupation, obj[3]: Restaurant20to50, obj[4]: Distance
	# {"feature": "Coupon", "instances": 127, "metric_value": 0.9964, "depth": 1}
	if obj[0]>1:
		# {"feature": "Education", "instances": 87, "metric_value": 0.9653, "depth": 2}
		if obj[1]>0:
			# {"feature": "Distance", "instances": 54, "metric_value": 0.999, "depth": 3}
			if obj[4]>1:
				# {"feature": "Restaurant20to50", "instances": 29, "metric_value": 0.9576, "depth": 4}
				if obj[3]<=2.0:
					# {"feature": "Occupation", "instances": 26, "metric_value": 0.8905, "depth": 5}
					if obj[2]<=13:
						return 'False'
					elif obj[2]>13:
						return 'True'
					else: return 'True'
				elif obj[3]>2.0:
					return 'True'
				else: return 'True'
			elif obj[4]<=1:
				# {"feature": "Occupation", "instances": 25, "metric_value": 0.9044, "depth": 4}
				if obj[2]>1:
					# {"feature": "Restaurant20to50", "instances": 22, "metric_value": 0.9457, "depth": 5}
					if obj[3]<=1.0:
						return 'True'
					elif obj[3]>1.0:
						return 'True'
					else: return 'True'
				elif obj[2]<=1:
					return 'True'
				else: return 'True'
			else: return 'True'
		elif obj[1]<=0:
			# {"feature": "Restaurant20to50", "instances": 33, "metric_value": 0.799, "depth": 3}
			if obj[3]<=1.0:
				# {"feature": "Occupation", "instances": 24, "metric_value": 0.9183, "depth": 4}
				if obj[2]>0:
					# {"feature": "Distance", "instances": 23, "metric_value": 0.8865, "depth": 5}
					if obj[4]<=2:
						return 'True'
					elif obj[4]>2:
						return 'True'
					else: return 'True'
				elif obj[2]<=0:
					return 'False'
				else: return 'False'
			elif obj[3]>1.0:
				return 'True'
			else: return 'True'
		else: return 'True'
	elif obj[0]<=1:
		# {"feature": "Occupation", "instances": 40, "metric_value": 0.9544, "depth": 2}
		if obj[2]<=16:
			# {"feature": "Restaurant20to50", "instances": 35, "metric_value": 0.9852, "depth": 3}
			if obj[3]>0.0:
				# {"feature": "Education", "instances": 29, "metric_value": 0.9991, "depth": 4}
				if obj[1]>0:
					# {"feature": "Distance", "instances": 18, "metric_value": 0.9911, "depth": 5}
					if obj[4]<=2:
						return 'False'
					elif obj[4]>2:
						return 'True'
					else: return 'True'
				elif obj[1]<=0:
					# {"feature": "Distance", "instances": 11, "metric_value": 0.9457, "depth": 5}
					if obj[4]<=2:
						return 'False'
					elif obj[4]>2:
						return 'False'
					else: return 'False'
				else: return 'False'
			elif obj[3]<=0.0:
				# {"feature": "Education", "instances": 6, "metric_value": 0.65, "depth": 4}
				if obj[1]>0:
					# {"feature": "Distance", "instances": 4, "metric_value": 0.8113, "depth": 5}
					if obj[4]>1:
						return 'False'
					elif obj[4]<=1:
						return 'False'
					else: return 'False'
				elif obj[1]<=0:
					return 'False'
				else: return 'False'
			else: return 'False'
		elif obj[2]>16:
			return 'False'
		else: return 'False'
	else: return 'False'
