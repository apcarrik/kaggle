def findDecision(obj): #obj[0]: Passanger, obj[1]: Coupon, obj[2]: Education, obj[3]: Occupation, obj[4]: Restaurant20to50, obj[5]: Direction_same, obj[6]: Distance
	# {"feature": "Passanger", "instances": 51, "metric_value": 0.9526, "depth": 1}
	if obj[0]<=2:
		# {"feature": "Distance", "instances": 37, "metric_value": 0.9953, "depth": 2}
		if obj[6]<=2:
			# {"feature": "Coupon", "instances": 35, "metric_value": 0.9852, "depth": 3}
			if obj[1]>0:
				# {"feature": "Restaurant20to50", "instances": 31, "metric_value": 0.9629, "depth": 4}
				if obj[4]<=1.0:
					# {"feature": "Occupation", "instances": 21, "metric_value": 0.9984, "depth": 5}
					if obj[3]<=6:
						# {"feature": "Education", "instances": 14, "metric_value": 0.9403, "depth": 6}
						if obj[2]<=2:
							# {"feature": "Direction_same", "instances": 13, "metric_value": 0.8905, "depth": 7}
							if obj[5]<=0:
								return 'True'
							elif obj[5]>0:
								return 'True'
							else: return 'True'
						elif obj[2]>2:
							return 'False'
						else: return 'False'
					elif obj[3]>6:
						# {"feature": "Direction_same", "instances": 7, "metric_value": 0.8631, "depth": 6}
						if obj[5]<=0:
							# {"feature": "Education", "instances": 6, "metric_value": 0.9183, "depth": 7}
							if obj[2]>0:
								return 'False'
							elif obj[2]<=0:
								return 'True'
							else: return 'True'
						elif obj[5]>0:
							return 'False'
						else: return 'False'
					else: return 'False'
				elif obj[4]>1.0:
					# {"feature": "Occupation", "instances": 10, "metric_value": 0.7219, "depth": 5}
					if obj[3]>3:
						# {"feature": "Direction_same", "instances": 7, "metric_value": 0.8631, "depth": 6}
						if obj[5]<=0:
							# {"feature": "Education", "instances": 6, "metric_value": 0.9183, "depth": 7}
							if obj[2]>0:
								return 'True'
							elif obj[2]<=0:
								return 'True'
							else: return 'True'
						elif obj[5]>0:
							return 'True'
						else: return 'True'
					elif obj[3]<=3:
						return 'True'
					else: return 'True'
				else: return 'True'
			elif obj[1]<=0:
				# {"feature": "Education", "instances": 4, "metric_value": 0.8113, "depth": 4}
				if obj[2]<=3:
					return 'False'
				elif obj[2]>3:
					return 'True'
				else: return 'True'
			else: return 'False'
		elif obj[6]>2:
			return 'False'
		else: return 'False'
	elif obj[0]>2:
		# {"feature": "Distance", "instances": 14, "metric_value": 0.5917, "depth": 2}
		if obj[6]>1:
			return 'True'
		elif obj[6]<=1:
			# {"feature": "Education", "instances": 7, "metric_value": 0.8631, "depth": 3}
			if obj[2]<=0:
				# {"feature": "Coupon", "instances": 4, "metric_value": 1.0, "depth": 4}
				if obj[1]>0:
					# {"feature": "Occupation", "instances": 3, "metric_value": 0.9183, "depth": 5}
					if obj[3]>0:
						# {"feature": "Restaurant20to50", "instances": 2, "metric_value": 1.0, "depth": 6}
						if obj[4]<=1.0:
							# {"feature": "Direction_same", "instances": 2, "metric_value": 1.0, "depth": 7}
							if obj[5]<=0:
								return 'False'
							else: return 'False'
						else: return 'False'
					elif obj[3]<=0:
						return 'True'
					else: return 'True'
				elif obj[1]<=0:
					return 'False'
				else: return 'False'
			elif obj[2]>0:
				return 'True'
			else: return 'True'
		else: return 'True'
	else: return 'True'
