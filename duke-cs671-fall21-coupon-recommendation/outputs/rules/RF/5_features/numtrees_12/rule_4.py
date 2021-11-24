def findDecision(obj): #obj[0]: Coupon, obj[1]: Education, obj[2]: Occupation, obj[3]: Restaurant20to50, obj[4]: Distance
	# {"feature": "Restaurant20to50", "instances": 85, "metric_value": 0.9951, "depth": 1}
	if obj[3]<=1.0:
		# {"feature": "Occupation", "instances": 48, "metric_value": 0.9799, "depth": 2}
		if obj[2]>2:
			# {"feature": "Education", "instances": 37, "metric_value": 0.909, "depth": 3}
			if obj[1]>1:
				# {"feature": "Coupon", "instances": 19, "metric_value": 0.6292, "depth": 4}
				if obj[0]<=2:
					return 'False'
				elif obj[0]>2:
					# {"feature": "Distance", "instances": 9, "metric_value": 0.9183, "depth": 5}
					if obj[4]>1:
						return 'False'
					elif obj[4]<=1:
						return 'True'
					else: return 'True'
				else: return 'False'
			elif obj[1]<=1:
				# {"feature": "Coupon", "instances": 18, "metric_value": 1.0, "depth": 4}
				if obj[0]>0:
					# {"feature": "Distance", "instances": 17, "metric_value": 0.9975, "depth": 5}
					if obj[4]<=2:
						return 'True'
					elif obj[4]>2:
						return 'False'
					else: return 'False'
				elif obj[0]<=0:
					return 'False'
				else: return 'False'
			else: return 'True'
		elif obj[2]<=2:
			# {"feature": "Distance", "instances": 11, "metric_value": 0.8454, "depth": 3}
			if obj[4]>1:
				# {"feature": "Coupon", "instances": 9, "metric_value": 0.5033, "depth": 4}
				if obj[0]<=3:
					return 'True'
				elif obj[0]>3:
					# {"feature": "Education", "instances": 2, "metric_value": 1.0, "depth": 5}
					if obj[1]>0:
						return 'False'
					elif obj[1]<=0:
						return 'True'
					else: return 'True'
				else: return 'False'
			elif obj[4]<=1:
				return 'False'
			else: return 'False'
		else: return 'True'
	elif obj[3]>1.0:
		# {"feature": "Occupation", "instances": 37, "metric_value": 0.878, "depth": 2}
		if obj[2]<=9:
			# {"feature": "Distance", "instances": 28, "metric_value": 0.7496, "depth": 3}
			if obj[4]<=2:
				# {"feature": "Coupon", "instances": 27, "metric_value": 0.6913, "depth": 4}
				if obj[0]<=3:
					# {"feature": "Education", "instances": 20, "metric_value": 0.6098, "depth": 5}
					if obj[1]>1:
						return 'True'
					elif obj[1]<=1:
						return 'True'
					else: return 'True'
				elif obj[0]>3:
					# {"feature": "Education", "instances": 7, "metric_value": 0.8631, "depth": 5}
					if obj[1]>1:
						return 'True'
					elif obj[1]<=1:
						return 'False'
					else: return 'False'
				else: return 'True'
			elif obj[4]>2:
				return 'False'
			else: return 'False'
		elif obj[2]>9:
			# {"feature": "Education", "instances": 9, "metric_value": 0.9911, "depth": 3}
			if obj[1]>0:
				# {"feature": "Coupon", "instances": 7, "metric_value": 0.8631, "depth": 4}
				if obj[0]>0:
					# {"feature": "Distance", "instances": 6, "metric_value": 0.65, "depth": 5}
					if obj[4]>1:
						return 'False'
					elif obj[4]<=1:
						return 'False'
					else: return 'False'
				elif obj[0]<=0:
					return 'True'
				else: return 'True'
			elif obj[1]<=0:
				return 'True'
			else: return 'True'
		else: return 'False'
	else: return 'True'
