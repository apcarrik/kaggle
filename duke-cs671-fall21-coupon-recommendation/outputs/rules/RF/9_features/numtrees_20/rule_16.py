def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Education, obj[4]: Occupation, obj[5]: Bar, obj[6]: Restaurant20to50, obj[7]: Direction_same, obj[8]: Distance
	# {"feature": "Coupon", "instances": 51, "metric_value": 0.9997, "depth": 1}
	if obj[2]>1:
		# {"feature": "Occupation", "instances": 36, "metric_value": 0.9436, "depth": 2}
		if obj[4]<=18:
			# {"feature": "Direction_same", "instances": 33, "metric_value": 0.9673, "depth": 3}
			if obj[7]<=0:
				# {"feature": "Time", "instances": 27, "metric_value": 0.9183, "depth": 4}
				if obj[1]>0:
					# {"feature": "Education", "instances": 20, "metric_value": 0.8113, "depth": 5}
					if obj[3]<=3:
						# {"feature": "Restaurant20to50", "instances": 19, "metric_value": 0.7425, "depth": 6}
						if obj[6]<=2.0:
							# {"feature": "Passanger", "instances": 17, "metric_value": 0.6723, "depth": 7}
							if obj[0]<=2:
								# {"feature": "Bar", "instances": 12, "metric_value": 0.8113, "depth": 8}
								if obj[5]<=1.0:
									# {"feature": "Distance", "instances": 10, "metric_value": 0.8813, "depth": 9}
									if obj[8]<=2:
										return 'True'
									elif obj[8]>2:
										return 'True'
									else: return 'True'
								elif obj[5]>1.0:
									return 'True'
								else: return 'True'
							elif obj[0]>2:
								return 'True'
							else: return 'True'
						elif obj[6]>2.0:
							# {"feature": "Passanger", "instances": 2, "metric_value": 1.0, "depth": 7}
							if obj[0]>2:
								return 'False'
							elif obj[0]<=2:
								return 'True'
							else: return 'True'
						else: return 'False'
					elif obj[3]>3:
						return 'False'
					else: return 'False'
				elif obj[1]<=0:
					# {"feature": "Education", "instances": 7, "metric_value": 0.9852, "depth": 5}
					if obj[3]>0:
						# {"feature": "Passanger", "instances": 5, "metric_value": 0.7219, "depth": 6}
						if obj[0]>0:
							return 'False'
						elif obj[0]<=0:
							return 'True'
						else: return 'True'
					elif obj[3]<=0:
						return 'True'
					else: return 'True'
				else: return 'False'
			elif obj[7]>0:
				# {"feature": "Bar", "instances": 6, "metric_value": 0.9183, "depth": 4}
				if obj[5]>0.0:
					# {"feature": "Time", "instances": 4, "metric_value": 1.0, "depth": 5}
					if obj[1]>0:
						# {"feature": "Education", "instances": 3, "metric_value": 0.9183, "depth": 6}
						if obj[3]<=2:
							# {"feature": "Passanger", "instances": 2, "metric_value": 1.0, "depth": 7}
							if obj[0]<=1:
								# {"feature": "Restaurant20to50", "instances": 2, "metric_value": 1.0, "depth": 8}
								if obj[6]<=2.0:
									# {"feature": "Distance", "instances": 2, "metric_value": 1.0, "depth": 9}
									if obj[8]<=1:
										return 'False'
									else: return 'False'
								else: return 'False'
							else: return 'False'
						elif obj[3]>2:
							return 'False'
						else: return 'False'
					elif obj[1]<=0:
						return 'True'
					else: return 'True'
				elif obj[5]<=0.0:
					return 'False'
				else: return 'False'
			else: return 'False'
		elif obj[4]>18:
			return 'True'
		else: return 'True'
	elif obj[2]<=1:
		# {"feature": "Passanger", "instances": 15, "metric_value": 0.7219, "depth": 2}
		if obj[0]<=1:
			return 'False'
		elif obj[0]>1:
			# {"feature": "Restaurant20to50", "instances": 5, "metric_value": 0.971, "depth": 3}
			if obj[6]>1.0:
				return 'True'
			elif obj[6]<=1.0:
				return 'False'
			else: return 'False'
		else: return 'True'
	else: return 'False'
