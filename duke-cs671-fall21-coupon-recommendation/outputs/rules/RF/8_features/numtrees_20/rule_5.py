def findDecision(obj): #obj[0]: Passanger, obj[1]: Coupon, obj[2]: Education, obj[3]: Occupation, obj[4]: Bar, obj[5]: Restaurant20to50, obj[6]: Direction_same, obj[7]: Distance
	# {"feature": "Direction_same", "instances": 51, "metric_value": 0.9931, "depth": 1}
	if obj[6]<=0:
		# {"feature": "Occupation", "instances": 42, "metric_value": 0.9737, "depth": 2}
		if obj[3]>5:
			# {"feature": "Passanger", "instances": 30, "metric_value": 0.9183, "depth": 3}
			if obj[0]<=2:
				# {"feature": "Coupon", "instances": 19, "metric_value": 0.9819, "depth": 4}
				if obj[1]>2:
					# {"feature": "Bar", "instances": 12, "metric_value": 0.8113, "depth": 5}
					if obj[4]<=1.0:
						# {"feature": "Distance", "instances": 8, "metric_value": 0.9544, "depth": 6}
						if obj[7]>1:
							# {"feature": "Education", "instances": 6, "metric_value": 1.0, "depth": 7}
							if obj[2]>0:
								# {"feature": "Restaurant20to50", "instances": 5, "metric_value": 0.971, "depth": 8}
								if obj[5]<=2.0:
									return 'True'
								elif obj[5]>2.0:
									return 'False'
								else: return 'False'
							elif obj[2]<=0:
								return 'False'
							else: return 'False'
						elif obj[7]<=1:
							return 'True'
						else: return 'True'
					elif obj[4]>1.0:
						return 'True'
					else: return 'True'
				elif obj[1]<=2:
					# {"feature": "Bar", "instances": 7, "metric_value": 0.8631, "depth": 5}
					if obj[4]>0.0:
						# {"feature": "Education", "instances": 6, "metric_value": 0.65, "depth": 6}
						if obj[2]>0:
							return 'False'
						elif obj[2]<=0:
							# {"feature": "Restaurant20to50", "instances": 3, "metric_value": 0.9183, "depth": 7}
							if obj[5]<=1.0:
								# {"feature": "Distance", "instances": 3, "metric_value": 0.9183, "depth": 8}
								if obj[7]<=1:
									return 'False'
								else: return 'False'
							else: return 'False'
						else: return 'False'
					elif obj[4]<=0.0:
						return 'True'
					else: return 'True'
				else: return 'False'
			elif obj[0]>2:
				# {"feature": "Coupon", "instances": 11, "metric_value": 0.684, "depth": 4}
				if obj[1]<=3:
					return 'True'
				elif obj[1]>3:
					# {"feature": "Education", "instances": 4, "metric_value": 1.0, "depth": 5}
					if obj[2]<=0:
						return 'True'
					elif obj[2]>0:
						return 'False'
					else: return 'False'
				else: return 'True'
			else: return 'True'
		elif obj[3]<=5:
			# {"feature": "Bar", "instances": 12, "metric_value": 0.9799, "depth": 3}
			if obj[4]<=0.0:
				# {"feature": "Coupon", "instances": 9, "metric_value": 0.9911, "depth": 4}
				if obj[1]>3:
					# {"feature": "Passanger", "instances": 5, "metric_value": 0.7219, "depth": 5}
					if obj[0]<=1:
						return 'False'
					elif obj[0]>1:
						# {"feature": "Education", "instances": 2, "metric_value": 1.0, "depth": 6}
						if obj[2]>0:
							return 'False'
						elif obj[2]<=0:
							return 'True'
						else: return 'True'
					else: return 'False'
				elif obj[1]<=3:
					return 'True'
				else: return 'True'
			elif obj[4]>0.0:
				return 'False'
			else: return 'False'
		else: return 'False'
	elif obj[6]>0:
		# {"feature": "Distance", "instances": 9, "metric_value": 0.9183, "depth": 2}
		if obj[7]<=1:
			return 'False'
		elif obj[7]>1:
			# {"feature": "Occupation", "instances": 4, "metric_value": 0.8113, "depth": 3}
			if obj[3]<=10:
				# {"feature": "Coupon", "instances": 2, "metric_value": 1.0, "depth": 4}
				if obj[1]<=0:
					return 'False'
				elif obj[1]>0:
					return 'True'
				else: return 'True'
			elif obj[3]>10:
				return 'True'
			else: return 'True'
		else: return 'True'
	else: return 'False'
