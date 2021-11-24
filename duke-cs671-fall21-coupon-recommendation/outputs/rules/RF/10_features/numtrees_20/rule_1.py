def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Education, obj[4]: Occupation, obj[5]: Bar, obj[6]: Coffeehouse, obj[7]: Restaurant20to50, obj[8]: Direction_same, obj[9]: Distance
	# {"feature": "Time", "instances": 51, "metric_value": 0.9774, "depth": 1}
	if obj[1]<=3:
		# {"feature": "Occupation", "instances": 39, "metric_value": 0.9995, "depth": 2}
		if obj[4]<=12:
			# {"feature": "Coupon", "instances": 36, "metric_value": 0.9911, "depth": 3}
			if obj[2]<=3:
				# {"feature": "Education", "instances": 28, "metric_value": 0.9403, "depth": 4}
				if obj[3]>0:
					# {"feature": "Restaurant20to50", "instances": 22, "metric_value": 0.994, "depth": 5}
					if obj[7]>-1.0:
						# {"feature": "Direction_same", "instances": 21, "metric_value": 0.9852, "depth": 6}
						if obj[8]<=0:
							# {"feature": "Coffeehouse", "instances": 15, "metric_value": 0.9183, "depth": 7}
							if obj[6]<=1.0:
								# {"feature": "Passanger", "instances": 8, "metric_value": 0.5436, "depth": 8}
								if obj[0]<=1:
									return 'True'
								elif obj[0]>1:
									# {"feature": "Distance", "instances": 3, "metric_value": 0.9183, "depth": 9}
									if obj[9]>1:
										# {"feature": "Bar", "instances": 2, "metric_value": 1.0, "depth": 10}
										if obj[5]<=0.0:
											return 'True'
										else: return 'True'
									elif obj[9]<=1:
										return 'True'
									else: return 'True'
								else: return 'True'
							elif obj[6]>1.0:
								# {"feature": "Distance", "instances": 7, "metric_value": 0.9852, "depth": 8}
								if obj[9]>1:
									# {"feature": "Bar", "instances": 6, "metric_value": 0.9183, "depth": 9}
									if obj[5]>0.0:
										# {"feature": "Passanger", "instances": 4, "metric_value": 0.8113, "depth": 10}
										if obj[0]<=1:
											return 'False'
										elif obj[0]>1:
											return 'True'
										else: return 'True'
									elif obj[5]<=0.0:
										# {"feature": "Passanger", "instances": 2, "metric_value": 1.0, "depth": 10}
										if obj[0]<=1:
											return 'True'
										elif obj[0]>1:
											return 'False'
										else: return 'False'
									else: return 'True'
								elif obj[9]<=1:
									return 'True'
								else: return 'True'
							else: return 'False'
						elif obj[8]>0:
							# {"feature": "Coffeehouse", "instances": 6, "metric_value": 0.9183, "depth": 7}
							if obj[6]<=1.0:
								# {"feature": "Bar", "instances": 5, "metric_value": 0.7219, "depth": 8}
								if obj[5]<=0.0:
									# {"feature": "Passanger", "instances": 4, "metric_value": 0.8113, "depth": 9}
									if obj[0]<=1:
										# {"feature": "Distance", "instances": 4, "metric_value": 0.8113, "depth": 10}
										if obj[9]<=1:
											return 'False'
										else: return 'False'
									else: return 'False'
								elif obj[5]>0.0:
									return 'False'
								else: return 'False'
							elif obj[6]>1.0:
								return 'True'
							else: return 'True'
						else: return 'False'
					elif obj[7]<=-1.0:
						return 'False'
					else: return 'False'
				elif obj[3]<=0:
					return 'True'
				else: return 'True'
			elif obj[2]>3:
				# {"feature": "Passanger", "instances": 8, "metric_value": 0.8113, "depth": 4}
				if obj[0]<=1:
					return 'False'
				elif obj[0]>1:
					# {"feature": "Distance", "instances": 4, "metric_value": 1.0, "depth": 5}
					if obj[9]<=1:
						return 'False'
					elif obj[9]>1:
						return 'True'
					else: return 'True'
				else: return 'False'
			else: return 'False'
		elif obj[4]>12:
			return 'False'
		else: return 'False'
	elif obj[1]>3:
		# {"feature": "Passanger", "instances": 12, "metric_value": 0.65, "depth": 2}
		if obj[0]>1:
			return 'True'
		elif obj[0]<=1:
			# {"feature": "Education", "instances": 3, "metric_value": 0.9183, "depth": 3}
			if obj[3]<=0:
				return 'False'
			elif obj[3]>0:
				return 'True'
			else: return 'True'
		else: return 'False'
	else: return 'True'
