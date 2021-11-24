def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Age, obj[4]: Education, obj[5]: Occupation, obj[6]: Bar, obj[7]: Coffeehouse, obj[8]: Restaurant20to50, obj[9]: Direction_same, obj[10]: Distance
	# {"feature": "Occupation", "instances": 34, "metric_value": 0.9774, "depth": 1}
	if obj[5]<=8:
		# {"feature": "Passanger", "instances": 29, "metric_value": 0.9991, "depth": 2}
		if obj[0]<=1:
			# {"feature": "Bar", "instances": 20, "metric_value": 0.9341, "depth": 3}
			if obj[6]>-1.0:
				# {"feature": "Age", "instances": 18, "metric_value": 0.8524, "depth": 4}
				if obj[3]>0:
					# {"feature": "Time", "instances": 17, "metric_value": 0.7871, "depth": 5}
					if obj[1]>0:
						# {"feature": "Direction_same", "instances": 14, "metric_value": 0.8631, "depth": 6}
						if obj[9]<=0:
							# {"feature": "Coupon", "instances": 12, "metric_value": 0.65, "depth": 7}
							if obj[2]<=1:
								# {"feature": "Education", "instances": 7, "metric_value": 0.8631, "depth": 8}
								if obj[4]>0:
									# {"feature": "Distance", "instances": 6, "metric_value": 0.9183, "depth": 9}
									if obj[10]<=1:
										# {"feature": "Coffeehouse", "instances": 5, "metric_value": 0.971, "depth": 10}
										if obj[7]<=0.0:
											# {"feature": "Restaurant20to50", "instances": 4, "metric_value": 0.8113, "depth": 11}
											if obj[8]<=1.0:
												return 'False'
											elif obj[8]>1.0:
												return 'False'
											else: return 'False'
										elif obj[7]>0.0:
											return 'True'
										else: return 'True'
									elif obj[10]>1:
										return 'False'
									else: return 'False'
								elif obj[4]<=0:
									return 'False'
								else: return 'False'
							elif obj[2]>1:
								return 'False'
							else: return 'False'
						elif obj[9]>0:
							return 'True'
						else: return 'True'
					elif obj[1]<=0:
						return 'False'
					else: return 'False'
				elif obj[3]<=0:
					return 'True'
				else: return 'True'
			elif obj[6]<=-1.0:
				return 'True'
			else: return 'True'
		elif obj[0]>1:
			# {"feature": "Time", "instances": 9, "metric_value": 0.7642, "depth": 3}
			if obj[1]<=2:
				return 'True'
			elif obj[1]>2:
				# {"feature": "Bar", "instances": 3, "metric_value": 0.9183, "depth": 4}
				if obj[6]>0.0:
					return 'False'
				elif obj[6]<=0.0:
					return 'True'
				else: return 'True'
			else: return 'False'
		else: return 'True'
	elif obj[5]>8:
		return 'False'
	else: return 'False'
