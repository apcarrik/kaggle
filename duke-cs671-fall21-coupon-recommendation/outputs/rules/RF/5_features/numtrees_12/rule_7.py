def findDecision(obj): #obj[0]: Coupon, obj[1]: Education, obj[2]: Occupation, obj[3]: Restaurant20to50, obj[4]: Distance
	# {"feature": "Distance", "instances": 85, "metric_value": 0.9951, "depth": 1}
	if obj[4]<=2:
		# {"feature": "Coupon", "instances": 76, "metric_value": 0.9819, "depth": 2}
		if obj[0]<=2:
			# {"feature": "Occupation", "instances": 42, "metric_value": 1.0, "depth": 3}
			if obj[2]<=12:
				# {"feature": "Education", "instances": 29, "metric_value": 0.9784, "depth": 4}
				if obj[1]<=3:
					# {"feature": "Restaurant20to50", "instances": 28, "metric_value": 0.9666, "depth": 5}
					if obj[3]<=3.0:
						return 'False'
					elif obj[3]>3.0:
						return 'False'
					else: return 'False'
				elif obj[1]>3:
					return 'True'
				else: return 'True'
			elif obj[2]>12:
				# {"feature": "Education", "instances": 13, "metric_value": 0.8905, "depth": 4}
				if obj[1]>0:
					# {"feature": "Restaurant20to50", "instances": 9, "metric_value": 0.9911, "depth": 5}
					if obj[3]<=1.0:
						return 'True'
					elif obj[3]>1.0:
						return 'False'
					else: return 'False'
				elif obj[1]<=0:
					return 'True'
				else: return 'True'
			else: return 'True'
		elif obj[0]>2:
			# {"feature": "Occupation", "instances": 34, "metric_value": 0.9082, "depth": 3}
			if obj[2]<=16:
				# {"feature": "Restaurant20to50", "instances": 32, "metric_value": 0.9284, "depth": 4}
				if obj[3]<=1.0:
					# {"feature": "Education", "instances": 19, "metric_value": 0.9819, "depth": 5}
					if obj[1]<=2:
						return 'True'
					elif obj[1]>2:
						return 'True'
					else: return 'True'
				elif obj[3]>1.0:
					# {"feature": "Education", "instances": 13, "metric_value": 0.7793, "depth": 5}
					if obj[1]<=2:
						return 'True'
					elif obj[1]>2:
						return 'False'
					else: return 'False'
				else: return 'True'
			elif obj[2]>16:
				return 'True'
			else: return 'True'
		else: return 'True'
	elif obj[4]>2:
		# {"feature": "Restaurant20to50", "instances": 9, "metric_value": 0.7642, "depth": 2}
		if obj[3]>0.0:
			# {"feature": "Coupon", "instances": 8, "metric_value": 0.5436, "depth": 3}
			if obj[0]>0:
				return 'False'
			elif obj[0]<=0:
				# {"feature": "Education", "instances": 3, "metric_value": 0.9183, "depth": 4}
				if obj[1]<=1:
					return 'False'
				elif obj[1]>1:
					return 'True'
				else: return 'True'
			else: return 'False'
		elif obj[3]<=0.0:
			return 'True'
		else: return 'True'
	else: return 'False'
