def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Education, obj[4]: Occupation, obj[5]: Bar, obj[6]: Coffeehouse, obj[7]: Restaurant20to50, obj[8]: Direction_same, obj[9]: Distance
	# {"feature": "Occupation", "instances": 85, "metric_value": 0.9999, "depth": 1}
	if obj[4]<=21:
		# {"feature": "Bar", "instances": 82, "metric_value": 0.9983, "depth": 2}
		if obj[5]>-1.0:
			# {"feature": "Education", "instances": 80, "metric_value": 0.9959, "depth": 3}
			if obj[3]<=4:
				# {"feature": "Coffeehouse", "instances": 79, "metric_value": 0.9943, "depth": 4}
				if obj[6]>-1.0:
					# {"feature": "Restaurant20to50", "instances": 78, "metric_value": 0.9924, "depth": 5}
					if obj[7]>-1.0:
						# {"feature": "Passanger", "instances": 77, "metric_value": 0.9901, "depth": 6}
						if obj[0]>0:
							# {"feature": "Coupon", "instances": 73, "metric_value": 0.9836, "depth": 7}
							if obj[2]>1:
								# {"feature": "Direction_same", "instances": 59, "metric_value": 0.9981, "depth": 8}
								if obj[8]<=0:
									# {"feature": "Time", "instances": 50, "metric_value": 0.9988, "depth": 9}
									if obj[1]>1:
										# {"feature": "Distance", "instances": 25, "metric_value": 0.971, "depth": 10}
										if obj[9]>1:
											return 'True'
										elif obj[9]<=1:
											return 'True'
										else: return 'True'
									elif obj[1]<=1:
										# {"feature": "Distance", "instances": 25, "metric_value": 0.9896, "depth": 10}
										if obj[9]>1:
											return 'True'
										elif obj[9]<=1:
											return 'False'
										else: return 'False'
									else: return 'False'
								elif obj[8]>0:
									# {"feature": "Time", "instances": 9, "metric_value": 0.7642, "depth": 9}
									if obj[1]<=1:
										# {"feature": "Distance", "instances": 6, "metric_value": 0.9183, "depth": 10}
										if obj[9]<=1:
											return 'False'
										elif obj[9]>1:
											return 'False'
										else: return 'False'
									elif obj[1]>1:
										return 'False'
									else: return 'False'
								else: return 'False'
							elif obj[2]<=1:
								# {"feature": "Direction_same", "instances": 14, "metric_value": 0.7496, "depth": 8}
								if obj[8]<=0:
									# {"feature": "Time", "instances": 13, "metric_value": 0.6194, "depth": 9}
									if obj[1]<=3:
										# {"feature": "Distance", "instances": 10, "metric_value": 0.469, "depth": 10}
										if obj[9]<=2:
											return 'False'
										elif obj[9]>2:
											return 'False'
										else: return 'False'
									elif obj[1]>3:
										# {"feature": "Distance", "instances": 3, "metric_value": 0.9183, "depth": 10}
										if obj[9]<=1:
											return 'False'
										elif obj[9]>1:
											return 'False'
										else: return 'False'
									else: return 'False'
								elif obj[8]>0:
									return 'True'
								else: return 'True'
							else: return 'False'
						elif obj[0]<=0:
							# {"feature": "Time", "instances": 4, "metric_value": 0.8113, "depth": 7}
							if obj[1]<=0:
								# {"feature": "Distance", "instances": 2, "metric_value": 1.0, "depth": 8}
								if obj[9]>1:
									return 'True'
								elif obj[9]<=1:
									return 'False'
								else: return 'False'
							elif obj[1]>0:
								return 'True'
							else: return 'True'
						else: return 'True'
					elif obj[7]<=-1.0:
						return 'True'
					else: return 'True'
				elif obj[6]<=-1.0:
					return 'True'
				else: return 'True'
			elif obj[3]>4:
				return 'True'
			else: return 'True'
		elif obj[5]<=-1.0:
			return 'True'
		else: return 'True'
	elif obj[4]>21:
		return 'True'
	else: return 'True'
