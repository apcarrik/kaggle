def findDecision(obj): #obj[0]: Passanger, obj[1]: Coupon, obj[2]: Education, obj[3]: Occupation, obj[4]: Bar, obj[5]: Restaurant20to50, obj[6]: Direction_same, obj[7]: Distance
	# {"feature": "Education", "instances": 51, "metric_value": 0.8479, "depth": 1}
	if obj[2]<=2:
		# {"feature": "Occupation", "instances": 43, "metric_value": 0.9103, "depth": 2}
		if obj[3]>4:
			# {"feature": "Coupon", "instances": 29, "metric_value": 0.9923, "depth": 3}
			if obj[1]>0:
				# {"feature": "Distance", "instances": 26, "metric_value": 0.9612, "depth": 4}
				if obj[7]>1:
					# {"feature": "Passanger", "instances": 14, "metric_value": 0.8631, "depth": 5}
					if obj[0]<=2:
						# {"feature": "Bar", "instances": 9, "metric_value": 0.9911, "depth": 6}
						if obj[4]>0.0:
							# {"feature": "Restaurant20to50", "instances": 6, "metric_value": 1.0, "depth": 7}
							if obj[5]<=1.0:
								# {"feature": "Direction_same", "instances": 4, "metric_value": 1.0, "depth": 8}
								if obj[6]<=0:
									return 'False'
								elif obj[6]>0:
									return 'True'
								else: return 'True'
							elif obj[5]>1.0:
								# {"feature": "Direction_same", "instances": 2, "metric_value": 1.0, "depth": 8}
								if obj[6]>0:
									return 'False'
								elif obj[6]<=0:
									return 'True'
								else: return 'True'
							else: return 'False'
						elif obj[4]<=0.0:
							# {"feature": "Restaurant20to50", "instances": 3, "metric_value": 0.9183, "depth": 7}
							if obj[5]<=1.0:
								# {"feature": "Direction_same", "instances": 2, "metric_value": 1.0, "depth": 8}
								if obj[6]<=0:
									return 'False'
								else: return 'False'
							elif obj[5]>1.0:
								return 'True'
							else: return 'True'
						else: return 'True'
					elif obj[0]>2:
						return 'True'
					else: return 'True'
				elif obj[7]<=1:
					# {"feature": "Direction_same", "instances": 12, "metric_value": 1.0, "depth": 5}
					if obj[6]<=0:
						# {"feature": "Restaurant20to50", "instances": 8, "metric_value": 0.9544, "depth": 6}
						if obj[5]<=2.0:
							# {"feature": "Bar", "instances": 5, "metric_value": 0.7219, "depth": 7}
							if obj[4]<=0.0:
								return 'False'
							elif obj[4]>0.0:
								# {"feature": "Passanger", "instances": 2, "metric_value": 1.0, "depth": 8}
								if obj[0]<=1:
									return 'False'
								else: return 'False'
							else: return 'False'
						elif obj[5]>2.0:
							# {"feature": "Bar", "instances": 3, "metric_value": 0.9183, "depth": 7}
							if obj[4]<=0.0:
								return 'True'
							elif obj[4]>0.0:
								return 'False'
							else: return 'False'
						else: return 'True'
					elif obj[6]>0:
						# {"feature": "Bar", "instances": 4, "metric_value": 0.8113, "depth": 6}
						if obj[4]>0.0:
							return 'True'
						elif obj[4]<=0.0:
							# {"feature": "Restaurant20to50", "instances": 2, "metric_value": 1.0, "depth": 7}
							if obj[5]>0.0:
								return 'True'
							elif obj[5]<=0.0:
								return 'False'
							else: return 'False'
						else: return 'True'
					else: return 'True'
				else: return 'True'
			elif obj[1]<=0:
				return 'False'
			else: return 'False'
		elif obj[3]<=4:
			# {"feature": "Coupon", "instances": 14, "metric_value": 0.3712, "depth": 3}
			if obj[1]>2:
				return 'True'
			elif obj[1]<=2:
				# {"feature": "Bar", "instances": 4, "metric_value": 0.8113, "depth": 4}
				if obj[4]>0.0:
					return 'True'
				elif obj[4]<=0.0:
					# {"feature": "Restaurant20to50", "instances": 2, "metric_value": 1.0, "depth": 5}
					if obj[5]>0.0:
						return 'False'
					elif obj[5]<=0.0:
						return 'True'
					else: return 'True'
				else: return 'False'
			else: return 'True'
		else: return 'True'
	elif obj[2]>2:
		return 'True'
	else: return 'True'
