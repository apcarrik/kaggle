def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Age, obj[4]: Education, obj[5]: Occupation, obj[6]: Bar, obj[7]: Coffeehouse, obj[8]: Restaurant20to50, obj[9]: Direction_same, obj[10]: Distance
	# {"feature": "Passanger", "instances": 85, "metric_value": 0.9999, "depth": 1}
	if obj[0]<=1:
		# {"feature": "Distance", "instances": 45, "metric_value": 0.9183, "depth": 2}
		if obj[10]<=2:
			# {"feature": "Occupation", "instances": 39, "metric_value": 0.9612, "depth": 3}
			if obj[5]<=12:
				# {"feature": "Coffeehouse", "instances": 37, "metric_value": 0.9353, "depth": 4}
				if obj[7]<=3.0:
					# {"feature": "Age", "instances": 34, "metric_value": 0.9597, "depth": 5}
					if obj[3]>1:
						# {"feature": "Time", "instances": 21, "metric_value": 0.8631, "depth": 6}
						if obj[1]<=3:
							# {"feature": "Coupon", "instances": 17, "metric_value": 0.6723, "depth": 7}
							if obj[2]>1:
								# {"feature": "Restaurant20to50", "instances": 11, "metric_value": 0.8454, "depth": 8}
								if obj[8]>0.0:
									# {"feature": "Education", "instances": 10, "metric_value": 0.7219, "depth": 9}
									if obj[4]>0:
										# {"feature": "Bar", "instances": 5, "metric_value": 0.971, "depth": 10}
										if obj[6]<=1.0:
											# {"feature": "Direction_same", "instances": 3, "metric_value": 0.9183, "depth": 11}
											if obj[9]>0:
												return 'True'
											elif obj[9]<=0:
												return 'True'
											else: return 'True'
										elif obj[6]>1.0:
											return 'False'
										else: return 'False'
									elif obj[4]<=0:
										return 'False'
									else: return 'False'
								elif obj[8]<=0.0:
									return 'True'
								else: return 'True'
							elif obj[2]<=1:
								return 'False'
							else: return 'False'
						elif obj[1]>3:
							# {"feature": "Coupon", "instances": 4, "metric_value": 0.8113, "depth": 7}
							if obj[2]>3:
								# {"feature": "Restaurant20to50", "instances": 2, "metric_value": 1.0, "depth": 8}
								if obj[8]<=0.0:
									return 'False'
								elif obj[8]>0.0:
									return 'True'
								else: return 'True'
							elif obj[2]<=3:
								return 'True'
							else: return 'True'
						else: return 'True'
					elif obj[3]<=1:
						# {"feature": "Restaurant20to50", "instances": 13, "metric_value": 0.9957, "depth": 6}
						if obj[8]>0.0:
							# {"feature": "Time", "instances": 10, "metric_value": 0.8813, "depth": 7}
							if obj[1]<=3:
								# {"feature": "Coupon", "instances": 9, "metric_value": 0.7642, "depth": 8}
								if obj[2]>0:
									return 'True'
								elif obj[2]<=0:
									# {"feature": "Education", "instances": 4, "metric_value": 1.0, "depth": 9}
									if obj[4]<=2:
										# {"feature": "Bar", "instances": 3, "metric_value": 0.9183, "depth": 10}
										if obj[6]>0.0:
											# {"feature": "Direction_same", "instances": 2, "metric_value": 1.0, "depth": 11}
											if obj[9]<=0:
												return 'False'
											else: return 'False'
										elif obj[6]<=0.0:
											return 'False'
										else: return 'False'
									elif obj[4]>2:
										return 'True'
									else: return 'True'
								else: return 'False'
							elif obj[1]>3:
								return 'False'
							else: return 'False'
						elif obj[8]<=0.0:
							return 'False'
						else: return 'False'
					else: return 'True'
				elif obj[7]>3.0:
					return 'False'
				else: return 'False'
			elif obj[5]>12:
				return 'True'
			else: return 'True'
		elif obj[10]>2:
			return 'False'
		else: return 'False'
	elif obj[0]>1:
		# {"feature": "Time", "instances": 40, "metric_value": 0.9097, "depth": 2}
		if obj[1]<=3:
			# {"feature": "Bar", "instances": 30, "metric_value": 0.7219, "depth": 3}
			if obj[6]<=0.0:
				# {"feature": "Age", "instances": 16, "metric_value": 0.9544, "depth": 4}
				if obj[3]>3:
					# {"feature": "Coupon", "instances": 9, "metric_value": 0.5033, "depth": 5}
					if obj[2]>0:
						return 'True'
					elif obj[2]<=0:
						return 'False'
					else: return 'False'
				elif obj[3]<=3:
					# {"feature": "Education", "instances": 7, "metric_value": 0.8631, "depth": 5}
					if obj[4]<=1:
						# {"feature": "Occupation", "instances": 6, "metric_value": 0.65, "depth": 6}
						if obj[5]>0:
							return 'False'
						elif obj[5]<=0:
							# {"feature": "Coupon", "instances": 2, "metric_value": 1.0, "depth": 7}
							if obj[2]<=0:
								return 'False'
							elif obj[2]>0:
								return 'True'
							else: return 'True'
						else: return 'False'
					elif obj[4]>1:
						return 'True'
					else: return 'True'
				else: return 'False'
			elif obj[6]>0.0:
				return 'True'
			else: return 'True'
		elif obj[1]>3:
			# {"feature": "Bar", "instances": 10, "metric_value": 0.8813, "depth": 3}
			if obj[6]<=0.0:
				# {"feature": "Coffeehouse", "instances": 5, "metric_value": 0.971, "depth": 4}
				if obj[7]>1.0:
					return 'True'
				elif obj[7]<=1.0:
					return 'False'
				else: return 'False'
			elif obj[6]>0.0:
				return 'False'
			else: return 'False'
		else: return 'False'
	else: return 'True'
