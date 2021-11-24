def findDecision(obj): #obj[0]: Passanger, obj[1]: Coupon, obj[2]: Education, obj[3]: Occupation, obj[4]: Bar, obj[5]: Restaurant20to50, obj[6]: Direction_same, obj[7]: Distance
	# {"feature": "Coupon", "instances": 85, "metric_value": 0.9991, "depth": 1}
	if obj[1]>0:
		# {"feature": "Occupation", "instances": 75, "metric_value": 0.9844, "depth": 2}
		if obj[3]<=14:
			# {"feature": "Restaurant20to50", "instances": 70, "metric_value": 0.971, "depth": 3}
			if obj[5]>0.0:
				# {"feature": "Education", "instances": 61, "metric_value": 0.9905, "depth": 4}
				if obj[2]<=4:
					# {"feature": "Bar", "instances": 59, "metric_value": 0.9948, "depth": 5}
					if obj[4]<=1.0:
						# {"feature": "Distance", "instances": 39, "metric_value": 0.9612, "depth": 6}
						if obj[7]>1:
							# {"feature": "Passanger", "instances": 20, "metric_value": 1.0, "depth": 7}
							if obj[0]<=1:
								# {"feature": "Direction_same", "instances": 10, "metric_value": 0.8813, "depth": 8}
								if obj[6]<=0:
									return 'False'
								else: return 'False'
							elif obj[0]>1:
								# {"feature": "Direction_same", "instances": 10, "metric_value": 0.8813, "depth": 8}
								if obj[6]<=0:
									return 'True'
								else: return 'True'
							else: return 'True'
						elif obj[7]<=1:
							# {"feature": "Passanger", "instances": 19, "metric_value": 0.8315, "depth": 7}
							if obj[0]>0:
								# {"feature": "Direction_same", "instances": 17, "metric_value": 0.7871, "depth": 8}
								if obj[6]<=0:
									return 'True'
								elif obj[6]>0:
									return 'True'
								else: return 'True'
							elif obj[0]<=0:
								# {"feature": "Direction_same", "instances": 2, "metric_value": 1.0, "depth": 8}
								if obj[6]<=0:
									return 'True'
								else: return 'True'
							else: return 'True'
						else: return 'True'
					elif obj[4]>1.0:
						# {"feature": "Distance", "instances": 20, "metric_value": 0.971, "depth": 6}
						if obj[7]<=2:
							# {"feature": "Passanger", "instances": 18, "metric_value": 0.9911, "depth": 7}
							if obj[0]>0:
								# {"feature": "Direction_same", "instances": 17, "metric_value": 0.9774, "depth": 8}
								if obj[6]<=0:
									return 'False'
								elif obj[6]>0:
									return 'False'
								else: return 'False'
							elif obj[0]<=0:
								return 'True'
							else: return 'True'
						elif obj[7]>2:
							return 'False'
						else: return 'False'
					else: return 'False'
				elif obj[2]>4:
					return 'True'
				else: return 'True'
			elif obj[5]<=0.0:
				# {"feature": "Bar", "instances": 9, "metric_value": 0.5033, "depth": 4}
				if obj[4]<=1.0:
					return 'True'
				elif obj[4]>1.0:
					# {"feature": "Direction_same", "instances": 2, "metric_value": 1.0, "depth": 5}
					if obj[6]<=0:
						return 'False'
					elif obj[6]>0:
						return 'True'
					else: return 'True'
				else: return 'False'
			else: return 'True'
		elif obj[3]>14:
			# {"feature": "Passanger", "instances": 5, "metric_value": 0.7219, "depth": 3}
			if obj[0]<=2:
				return 'False'
			elif obj[0]>2:
				return 'True'
			else: return 'True'
		else: return 'False'
	elif obj[1]<=0:
		# {"feature": "Occupation", "instances": 10, "metric_value": 0.469, "depth": 2}
		if obj[3]<=6:
			return 'False'
		elif obj[3]>6:
			# {"feature": "Passanger", "instances": 2, "metric_value": 1.0, "depth": 3}
			if obj[0]>1:
				return 'True'
			elif obj[0]<=1:
				return 'False'
			else: return 'False'
		else: return 'True'
	else: return 'False'
