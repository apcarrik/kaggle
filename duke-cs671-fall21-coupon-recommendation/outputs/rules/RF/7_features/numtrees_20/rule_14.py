def findDecision(obj): #obj[0]: Passanger, obj[1]: Coupon, obj[2]: Education, obj[3]: Occupation, obj[4]: Restaurant20to50, obj[5]: Direction_same, obj[6]: Distance
	# {"feature": "Restaurant20to50", "instances": 51, "metric_value": 0.9997, "depth": 1}
	if obj[4]<=1.0:
		# {"feature": "Passanger", "instances": 33, "metric_value": 0.9457, "depth": 2}
		if obj[0]<=2:
			# {"feature": "Education", "instances": 20, "metric_value": 0.6098, "depth": 3}
			if obj[2]<=3:
				# {"feature": "Occupation", "instances": 19, "metric_value": 0.4855, "depth": 4}
				if obj[3]>1:
					# {"feature": "Distance", "instances": 18, "metric_value": 0.3095, "depth": 5}
					if obj[6]>1:
						return 'False'
					elif obj[6]<=1:
						# {"feature": "Coupon", "instances": 2, "metric_value": 1.0, "depth": 6}
						if obj[1]>0:
							return 'False'
						elif obj[1]<=0:
							return 'True'
						else: return 'True'
					else: return 'False'
				elif obj[3]<=1:
					return 'True'
				else: return 'True'
			elif obj[2]>3:
				return 'True'
			else: return 'True'
		elif obj[0]>2:
			# {"feature": "Coupon", "instances": 13, "metric_value": 0.8905, "depth": 3}
			if obj[1]>0:
				# {"feature": "Occupation", "instances": 12, "metric_value": 0.8113, "depth": 4}
				if obj[3]<=6:
					# {"feature": "Distance", "instances": 6, "metric_value": 1.0, "depth": 5}
					if obj[6]>1:
						# {"feature": "Education", "instances": 5, "metric_value": 0.971, "depth": 6}
						if obj[2]<=0:
							# {"feature": "Direction_same", "instances": 3, "metric_value": 0.9183, "depth": 7}
							if obj[5]<=0:
								return 'True'
							else: return 'True'
						elif obj[2]>0:
							# {"feature": "Direction_same", "instances": 2, "metric_value": 1.0, "depth": 7}
							if obj[5]<=0:
								return 'True'
							else: return 'True'
						else: return 'True'
					elif obj[6]<=1:
						return 'False'
					else: return 'False'
				elif obj[3]>6:
					return 'True'
				else: return 'True'
			elif obj[1]<=0:
				return 'False'
			else: return 'False'
		else: return 'True'
	elif obj[4]>1.0:
		# {"feature": "Passanger", "instances": 18, "metric_value": 0.8524, "depth": 2}
		if obj[0]<=1:
			# {"feature": "Coupon", "instances": 13, "metric_value": 0.9612, "depth": 3}
			if obj[1]>1:
				# {"feature": "Occupation", "instances": 11, "metric_value": 0.994, "depth": 4}
				if obj[3]>5:
					# {"feature": "Education", "instances": 9, "metric_value": 0.9183, "depth": 5}
					if obj[2]>0:
						# {"feature": "Direction_same", "instances": 6, "metric_value": 1.0, "depth": 6}
						if obj[5]<=0:
							# {"feature": "Distance", "instances": 4, "metric_value": 0.8113, "depth": 7}
							if obj[6]<=2:
								return 'False'
							elif obj[6]>2:
								return 'False'
							else: return 'False'
						elif obj[5]>0:
							return 'True'
						else: return 'True'
					elif obj[2]<=0:
						return 'True'
					else: return 'True'
				elif obj[3]<=5:
					return 'False'
				else: return 'False'
			elif obj[1]<=1:
				return 'True'
			else: return 'True'
		elif obj[0]>1:
			return 'True'
		else: return 'True'
	else: return 'True'
