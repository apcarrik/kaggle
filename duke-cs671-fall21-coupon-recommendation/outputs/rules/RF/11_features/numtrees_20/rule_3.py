def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Age, obj[4]: Education, obj[5]: Occupation, obj[6]: Bar, obj[7]: Coffeehouse, obj[8]: Restaurant20to50, obj[9]: Direction_same, obj[10]: Distance
	# {"feature": "Passanger", "instances": 51, "metric_value": 0.9997, "depth": 1}
	if obj[0]<=2:
		# {"feature": "Occupation", "instances": 38, "metric_value": 0.9678, "depth": 2}
		if obj[5]>1:
			# {"feature": "Coffeehouse", "instances": 35, "metric_value": 0.9275, "depth": 3}
			if obj[7]<=3.0:
				# {"feature": "Age", "instances": 33, "metric_value": 0.885, "depth": 4}
				if obj[3]>1:
					# {"feature": "Bar", "instances": 23, "metric_value": 0.7554, "depth": 5}
					if obj[6]<=2.0:
						# {"feature": "Restaurant20to50", "instances": 22, "metric_value": 0.684, "depth": 6}
						if obj[8]<=1.0:
							# {"feature": "Direction_same", "instances": 16, "metric_value": 0.8113, "depth": 7}
							if obj[9]<=0:
								# {"feature": "Coupon", "instances": 13, "metric_value": 0.8905, "depth": 8}
								if obj[2]>0:
									# {"feature": "Distance", "instances": 12, "metric_value": 0.9183, "depth": 9}
									if obj[10]<=2:
										# {"feature": "Time", "instances": 11, "metric_value": 0.9457, "depth": 10}
										if obj[1]<=3:
											# {"feature": "Education", "instances": 7, "metric_value": 0.8631, "depth": 11}
											if obj[4]<=1:
												return 'False'
											elif obj[4]>1:
												return 'False'
											else: return 'False'
										elif obj[1]>3:
											# {"feature": "Education", "instances": 4, "metric_value": 1.0, "depth": 11}
											if obj[4]<=2:
												return 'True'
											elif obj[4]>2:
												return 'True'
											else: return 'True'
										else: return 'True'
									elif obj[10]>2:
										return 'False'
									else: return 'False'
								elif obj[2]<=0:
									return 'False'
								else: return 'False'
							elif obj[9]>0:
								return 'False'
							else: return 'False'
						elif obj[8]>1.0:
							return 'False'
						else: return 'False'
					elif obj[6]>2.0:
						return 'True'
					else: return 'True'
				elif obj[3]<=1:
					# {"feature": "Bar", "instances": 10, "metric_value": 1.0, "depth": 5}
					if obj[6]<=2.0:
						# {"feature": "Distance", "instances": 8, "metric_value": 0.9544, "depth": 6}
						if obj[10]>1:
							# {"feature": "Time", "instances": 6, "metric_value": 1.0, "depth": 7}
							if obj[1]<=2:
								# {"feature": "Coupon", "instances": 5, "metric_value": 0.971, "depth": 8}
								if obj[2]<=2:
									# {"feature": "Education", "instances": 4, "metric_value": 0.8113, "depth": 9}
									if obj[4]>0:
										return 'True'
									elif obj[4]<=0:
										# {"feature": "Restaurant20to50", "instances": 2, "metric_value": 1.0, "depth": 10}
										if obj[8]<=1.0:
											# {"feature": "Direction_same", "instances": 2, "metric_value": 1.0, "depth": 11}
											if obj[9]<=0:
												return 'True'
											else: return 'True'
										else: return 'True'
									else: return 'True'
								elif obj[2]>2:
									return 'False'
								else: return 'False'
							elif obj[1]>2:
								return 'False'
							else: return 'False'
						elif obj[10]<=1:
							return 'True'
						else: return 'True'
					elif obj[6]>2.0:
						return 'False'
					else: return 'False'
				else: return 'True'
			elif obj[7]>3.0:
				return 'True'
			else: return 'True'
		elif obj[5]<=1:
			return 'True'
		else: return 'True'
	elif obj[0]>2:
		# {"feature": "Occupation", "instances": 13, "metric_value": 0.6194, "depth": 2}
		if obj[5]>2:
			return 'True'
		elif obj[5]<=2:
			# {"feature": "Age", "instances": 5, "metric_value": 0.971, "depth": 3}
			if obj[3]<=3:
				# {"feature": "Education", "instances": 3, "metric_value": 0.9183, "depth": 4}
				if obj[4]>0:
					return 'False'
				elif obj[4]<=0:
					return 'True'
				else: return 'True'
			elif obj[3]>3:
				return 'True'
			else: return 'True'
		else: return 'True'
	else: return 'True'
