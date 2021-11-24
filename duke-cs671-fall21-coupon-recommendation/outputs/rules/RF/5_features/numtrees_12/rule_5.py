def findDecision(obj): #obj[0]: Coupon, obj[1]: Education, obj[2]: Occupation, obj[3]: Restaurant20to50, obj[4]: Distance
	# {"feature": "Coupon", "instances": 85, "metric_value": 0.9975, "depth": 1}
	if obj[0]>1:
		# {"feature": "Restaurant20to50", "instances": 60, "metric_value": 0.9183, "depth": 2}
		if obj[3]<=2.0:
			# {"feature": "Occupation", "instances": 53, "metric_value": 0.9562, "depth": 3}
			if obj[2]>1:
				# {"feature": "Distance", "instances": 40, "metric_value": 0.9928, "depth": 4}
				if obj[4]<=2:
					# {"feature": "Education", "instances": 36, "metric_value": 0.9799, "depth": 5}
					if obj[1]>1:
						return 'True'
					elif obj[1]<=1:
						return 'True'
					else: return 'True'
				elif obj[4]>2:
					# {"feature": "Education", "instances": 4, "metric_value": 0.8113, "depth": 5}
					if obj[1]>0:
						return 'False'
					elif obj[1]<=0:
						return 'False'
					else: return 'False'
				else: return 'False'
			elif obj[2]<=1:
				# {"feature": "Distance", "instances": 13, "metric_value": 0.6194, "depth": 4}
				if obj[4]<=2:
					return 'True'
				elif obj[4]>2:
					# {"feature": "Education", "instances": 3, "metric_value": 0.9183, "depth": 5}
					if obj[1]<=0:
						return 'False'
					elif obj[1]>0:
						return 'True'
					else: return 'True'
				else: return 'False'
			else: return 'True'
		elif obj[3]>2.0:
			return 'True'
		else: return 'True'
	elif obj[0]<=1:
		# {"feature": "Education", "instances": 25, "metric_value": 0.7219, "depth": 2}
		if obj[1]<=2:
			# {"feature": "Distance", "instances": 19, "metric_value": 0.8315, "depth": 3}
			if obj[4]<=1:
				# {"feature": "Occupation", "instances": 10, "metric_value": 0.971, "depth": 4}
				if obj[2]<=13:
					# {"feature": "Restaurant20to50", "instances": 9, "metric_value": 0.9911, "depth": 5}
					if obj[3]>0.0:
						return 'False'
					elif obj[3]<=0.0:
						return 'False'
					else: return 'False'
				elif obj[2]>13:
					return 'False'
				else: return 'False'
			elif obj[4]>1:
				# {"feature": "Occupation", "instances": 9, "metric_value": 0.5033, "depth": 4}
				if obj[2]<=6:
					return 'False'
				elif obj[2]>6:
					# {"feature": "Restaurant20to50", "instances": 4, "metric_value": 0.8113, "depth": 5}
					if obj[3]<=1.0:
						return 'False'
					elif obj[3]>1.0:
						return 'False'
					else: return 'False'
				else: return 'False'
			else: return 'False'
		elif obj[1]>2:
			return 'False'
		else: return 'False'
	else: return 'False'
