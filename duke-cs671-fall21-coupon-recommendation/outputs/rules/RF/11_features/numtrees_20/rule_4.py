def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Age, obj[4]: Education, obj[5]: Occupation, obj[6]: Bar, obj[7]: Coffeehouse, obj[8]: Restaurant20to50, obj[9]: Direction_same, obj[10]: Distance
	# {"feature": "Occupation", "instances": 51, "metric_value": 0.9931, "depth": 1}
	if obj[5]<=9:
		# {"feature": "Education", "instances": 37, "metric_value": 0.9353, "depth": 2}
		if obj[4]<=3:
			# {"feature": "Time", "instances": 34, "metric_value": 0.874, "depth": 3}
			if obj[1]<=1:
				# {"feature": "Bar", "instances": 20, "metric_value": 0.9928, "depth": 4}
				if obj[6]<=1.0:
					# {"feature": "Coffeehouse", "instances": 15, "metric_value": 0.9183, "depth": 5}
					if obj[7]>1.0:
						# {"feature": "Coupon", "instances": 9, "metric_value": 0.5033, "depth": 6}
						if obj[2]>0:
							return 'True'
						elif obj[2]<=0:
							# {"feature": "Age", "instances": 2, "metric_value": 1.0, "depth": 7}
							if obj[3]<=1:
								return 'False'
							elif obj[3]>1:
								return 'True'
							else: return 'True'
						else: return 'False'
					elif obj[7]<=1.0:
						# {"feature": "Age", "instances": 6, "metric_value": 0.9183, "depth": 6}
						if obj[3]>4:
							# {"feature": "Direction_same", "instances": 5, "metric_value": 0.971, "depth": 7}
							if obj[9]<=0:
								# {"feature": "Coupon", "instances": 4, "metric_value": 0.8113, "depth": 8}
								if obj[2]<=2:
									# {"feature": "Restaurant20to50", "instances": 3, "metric_value": 0.9183, "depth": 9}
									if obj[8]>1.0:
										# {"feature": "Passanger", "instances": 2, "metric_value": 1.0, "depth": 10}
										if obj[0]<=1:
											# {"feature": "Distance", "instances": 2, "metric_value": 1.0, "depth": 11}
											if obj[10]<=3:
												return 'False'
											else: return 'False'
										else: return 'False'
									elif obj[8]<=1.0:
										return 'False'
									else: return 'False'
								elif obj[2]>2:
									return 'False'
								else: return 'False'
							elif obj[9]>0:
								return 'True'
							else: return 'True'
						elif obj[3]<=4:
							return 'False'
						else: return 'False'
					else: return 'False'
				elif obj[6]>1.0:
					# {"feature": "Coffeehouse", "instances": 5, "metric_value": 0.7219, "depth": 5}
					if obj[7]>0.0:
						return 'False'
					elif obj[7]<=0.0:
						return 'True'
					else: return 'True'
				else: return 'False'
			elif obj[1]>1:
				# {"feature": "Age", "instances": 14, "metric_value": 0.3712, "depth": 4}
				if obj[3]<=4:
					return 'True'
				elif obj[3]>4:
					# {"feature": "Restaurant20to50", "instances": 3, "metric_value": 0.9183, "depth": 5}
					if obj[8]<=1.0:
						return 'True'
					elif obj[8]>1.0:
						return 'False'
					else: return 'False'
				else: return 'True'
			else: return 'True'
		elif obj[4]>3:
			return 'False'
		else: return 'False'
	elif obj[5]>9:
		# {"feature": "Age", "instances": 14, "metric_value": 0.8631, "depth": 2}
		if obj[3]<=1:
			# {"feature": "Restaurant20to50", "instances": 7, "metric_value": 0.9852, "depth": 3}
			if obj[8]<=1.0:
				# {"feature": "Passanger", "instances": 4, "metric_value": 0.8113, "depth": 4}
				if obj[0]<=1:
					return 'False'
				elif obj[0]>1:
					return 'True'
				else: return 'True'
			elif obj[8]>1.0:
				return 'True'
			else: return 'True'
		elif obj[3]>1:
			return 'False'
		else: return 'False'
	else: return 'False'
