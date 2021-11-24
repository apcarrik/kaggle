def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Age, obj[4]: Education, obj[5]: Occupation, obj[6]: Bar, obj[7]: Coffeehouse, obj[8]: Restaurant20to50, obj[9]: Direction_same, obj[10]: Distance
	# {"feature": "Passanger", "instances": 85, "metric_value": 0.9919, "depth": 1}
	if obj[0]<=2:
		# {"feature": "Time", "instances": 64, "metric_value": 0.9972, "depth": 2}
		if obj[1]<=3:
			# {"feature": "Coupon", "instances": 58, "metric_value": 0.9862, "depth": 3}
			if obj[2]>1:
				# {"feature": "Education", "instances": 43, "metric_value": 0.9996, "depth": 4}
				if obj[4]>0:
					# {"feature": "Bar", "instances": 33, "metric_value": 0.9834, "depth": 5}
					if obj[6]>0.0:
						# {"feature": "Coffeehouse", "instances": 22, "metric_value": 0.994, "depth": 6}
						if obj[7]>0.0:
							# {"feature": "Age", "instances": 19, "metric_value": 0.998, "depth": 7}
							if obj[3]>0:
								# {"feature": "Occupation", "instances": 17, "metric_value": 0.9975, "depth": 8}
								if obj[5]>1:
									# {"feature": "Restaurant20to50", "instances": 16, "metric_value": 0.9887, "depth": 9}
									if obj[8]<=2.0:
										# {"feature": "Direction_same", "instances": 15, "metric_value": 0.9968, "depth": 10}
										if obj[9]<=0:
											# {"feature": "Distance", "instances": 10, "metric_value": 1.0, "depth": 11}
											if obj[10]>1:
												return 'False'
											elif obj[10]<=1:
												return 'False'
											else: return 'False'
										elif obj[9]>0:
											# {"feature": "Distance", "instances": 5, "metric_value": 0.971, "depth": 11}
											if obj[10]<=1:
												return 'False'
											else: return 'False'
										else: return 'False'
									elif obj[8]>2.0:
										return 'False'
									else: return 'False'
								elif obj[5]<=1:
									return 'True'
								else: return 'True'
							elif obj[3]<=0:
								return 'True'
							else: return 'True'
						elif obj[7]<=0.0:
							return 'False'
						else: return 'False'
					elif obj[6]<=0.0:
						# {"feature": "Age", "instances": 11, "metric_value": 0.684, "depth": 6}
						if obj[3]<=2:
							# {"feature": "Coffeehouse", "instances": 7, "metric_value": 0.8631, "depth": 7}
							if obj[7]<=3.0:
								# {"feature": "Direction_same", "instances": 6, "metric_value": 0.9183, "depth": 8}
								if obj[9]<=0:
									# {"feature": "Occupation", "instances": 5, "metric_value": 0.7219, "depth": 9}
									if obj[5]>1:
										return 'True'
									elif obj[5]<=1:
										# {"feature": "Distance", "instances": 2, "metric_value": 1.0, "depth": 10}
										if obj[10]<=2:
											return 'False'
										elif obj[10]>2:
											return 'True'
										else: return 'True'
									else: return 'False'
								elif obj[9]>0:
									return 'False'
								else: return 'False'
							elif obj[7]>3.0:
								return 'True'
							else: return 'True'
						elif obj[3]>2:
							return 'True'
						else: return 'True'
					else: return 'True'
				elif obj[4]<=0:
					# {"feature": "Occupation", "instances": 10, "metric_value": 0.8813, "depth": 5}
					if obj[5]<=10:
						# {"feature": "Coffeehouse", "instances": 6, "metric_value": 1.0, "depth": 6}
						if obj[7]<=1.0:
							# {"feature": "Restaurant20to50", "instances": 4, "metric_value": 0.8113, "depth": 7}
							if obj[8]>0.0:
								return 'False'
							elif obj[8]<=0.0:
								return 'True'
							else: return 'True'
						elif obj[7]>1.0:
							return 'True'
						else: return 'True'
					elif obj[5]>10:
						return 'False'
					else: return 'False'
				else: return 'False'
			elif obj[2]<=1:
				# {"feature": "Occupation", "instances": 15, "metric_value": 0.7219, "depth": 4}
				if obj[5]>2:
					return 'False'
				elif obj[5]<=2:
					# {"feature": "Bar", "instances": 5, "metric_value": 0.971, "depth": 5}
					if obj[6]<=0.0:
						# {"feature": "Age", "instances": 3, "metric_value": 0.9183, "depth": 6}
						if obj[3]>2:
							# {"feature": "Coffeehouse", "instances": 2, "metric_value": 1.0, "depth": 7}
							if obj[7]>1.0:
								return 'True'
							elif obj[7]<=1.0:
								return 'False'
							else: return 'False'
						elif obj[3]<=2:
							return 'False'
						else: return 'False'
					elif obj[6]>0.0:
						return 'True'
					else: return 'True'
				else: return 'True'
			else: return 'False'
		elif obj[1]>3:
			# {"feature": "Education", "instances": 6, "metric_value": 0.65, "depth": 3}
			if obj[4]<=3:
				return 'True'
			elif obj[4]>3:
				# {"feature": "Coupon", "instances": 2, "metric_value": 1.0, "depth": 4}
				if obj[2]>3:
					return 'True'
				elif obj[2]<=3:
					return 'False'
				else: return 'False'
			else: return 'True'
		else: return 'True'
	elif obj[0]>2:
		# {"feature": "Education", "instances": 21, "metric_value": 0.7025, "depth": 2}
		if obj[4]>0:
			# {"feature": "Time", "instances": 14, "metric_value": 0.8631, "depth": 3}
			if obj[1]>0:
				# {"feature": "Coffeehouse", "instances": 10, "metric_value": 0.971, "depth": 4}
				if obj[7]<=2.0:
					# {"feature": "Age", "instances": 8, "metric_value": 1.0, "depth": 5}
					if obj[3]>0:
						# {"feature": "Occupation", "instances": 7, "metric_value": 0.9852, "depth": 6}
						if obj[5]<=6:
							# {"feature": "Coupon", "instances": 6, "metric_value": 1.0, "depth": 7}
							if obj[2]>2:
								# {"feature": "Restaurant20to50", "instances": 3, "metric_value": 0.9183, "depth": 8}
								if obj[8]<=1.0:
									return 'False'
								elif obj[8]>1.0:
									return 'True'
								else: return 'True'
							elif obj[2]<=2:
								# {"feature": "Bar", "instances": 3, "metric_value": 0.9183, "depth": 8}
								if obj[6]<=0.0:
									# {"feature": "Restaurant20to50", "instances": 2, "metric_value": 1.0, "depth": 9}
									if obj[8]<=1.0:
										return 'True'
									elif obj[8]>1.0:
										return 'False'
									else: return 'False'
								elif obj[6]>0.0:
									return 'True'
								else: return 'True'
							else: return 'True'
						elif obj[5]>6:
							return 'True'
						else: return 'True'
					elif obj[3]<=0:
						return 'False'
					else: return 'False'
				elif obj[7]>2.0:
					return 'True'
				else: return 'True'
			elif obj[1]<=0:
				return 'True'
			else: return 'True'
		elif obj[4]<=0:
			return 'True'
		else: return 'True'
	else: return 'True'
