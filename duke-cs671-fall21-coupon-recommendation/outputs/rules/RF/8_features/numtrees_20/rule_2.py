def findDecision(obj): #obj[0]: Passanger, obj[1]: Coupon, obj[2]: Education, obj[3]: Occupation, obj[4]: Bar, obj[5]: Restaurant20to50, obj[6]: Direction_same, obj[7]: Distance
	# {"feature": "Bar", "instances": 51, "metric_value": 0.9931, "depth": 1}
	if obj[4]<=0.0:
		# {"feature": "Coupon", "instances": 29, "metric_value": 0.8936, "depth": 2}
		if obj[1]>1:
			# {"feature": "Occupation", "instances": 21, "metric_value": 0.9852, "depth": 3}
			if obj[3]>4:
				# {"feature": "Restaurant20to50", "instances": 14, "metric_value": 0.9852, "depth": 4}
				if obj[5]<=2.0:
					# {"feature": "Distance", "instances": 13, "metric_value": 0.9612, "depth": 5}
					if obj[7]<=2:
						# {"feature": "Passanger", "instances": 12, "metric_value": 0.9799, "depth": 6}
						if obj[0]>1:
							# {"feature": "Education", "instances": 8, "metric_value": 0.9544, "depth": 7}
							if obj[2]>0:
								# {"feature": "Direction_same", "instances": 5, "metric_value": 0.7219, "depth": 8}
								if obj[6]<=0:
									return 'True'
								else: return 'True'
							elif obj[2]<=0:
								# {"feature": "Direction_same", "instances": 3, "metric_value": 0.9183, "depth": 8}
								if obj[6]<=0:
									return 'False'
								else: return 'False'
							else: return 'False'
						elif obj[0]<=1:
							# {"feature": "Education", "instances": 4, "metric_value": 1.0, "depth": 7}
							if obj[2]>0:
								# {"feature": "Direction_same", "instances": 3, "metric_value": 0.9183, "depth": 8}
								if obj[6]<=0:
									return 'True'
								elif obj[6]>0:
									return 'False'
								else: return 'False'
							elif obj[2]<=0:
								return 'True'
							else: return 'True'
						else: return 'True'
					elif obj[7]>2:
						return 'True'
					else: return 'True'
				elif obj[5]>2.0:
					return 'False'
				else: return 'False'
			elif obj[3]<=4:
				# {"feature": "Passanger", "instances": 7, "metric_value": 0.5917, "depth": 4}
				if obj[0]<=2:
					return 'False'
				elif obj[0]>2:
					# {"feature": "Education", "instances": 2, "metric_value": 1.0, "depth": 5}
					if obj[2]>0:
						return 'True'
					elif obj[2]<=0:
						return 'False'
					else: return 'False'
				else: return 'True'
			else: return 'False'
		elif obj[1]<=1:
			return 'False'
		else: return 'False'
	elif obj[4]>0.0:
		# {"feature": "Occupation", "instances": 22, "metric_value": 0.9457, "depth": 2}
		if obj[3]<=8:
			# {"feature": "Education", "instances": 14, "metric_value": 0.7496, "depth": 3}
			if obj[2]>0:
				return 'True'
			elif obj[2]<=0:
				# {"feature": "Distance", "instances": 7, "metric_value": 0.9852, "depth": 4}
				if obj[7]>1:
					# {"feature": "Passanger", "instances": 5, "metric_value": 0.7219, "depth": 5}
					if obj[0]<=1:
						# {"feature": "Coupon", "instances": 3, "metric_value": 0.9183, "depth": 6}
						if obj[1]>0:
							# {"feature": "Restaurant20to50", "instances": 2, "metric_value": 1.0, "depth": 7}
							if obj[5]<=1.0:
								return 'False'
							elif obj[5]>1.0:
								return 'True'
							else: return 'True'
						elif obj[1]<=0:
							return 'True'
						else: return 'True'
					elif obj[0]>1:
						return 'True'
					else: return 'True'
				elif obj[7]<=1:
					return 'False'
				else: return 'False'
			else: return 'True'
		elif obj[3]>8:
			# {"feature": "Education", "instances": 8, "metric_value": 0.9544, "depth": 3}
			if obj[2]>0:
				# {"feature": "Restaurant20to50", "instances": 6, "metric_value": 0.65, "depth": 4}
				if obj[5]>0.0:
					return 'False'
				elif obj[5]<=0.0:
					# {"feature": "Passanger", "instances": 2, "metric_value": 1.0, "depth": 5}
					if obj[0]<=3:
						# {"feature": "Coupon", "instances": 2, "metric_value": 1.0, "depth": 6}
						if obj[1]<=2:
							# {"feature": "Direction_same", "instances": 2, "metric_value": 1.0, "depth": 7}
							if obj[6]<=0:
								# {"feature": "Distance", "instances": 2, "metric_value": 1.0, "depth": 8}
								if obj[7]<=2:
									return 'True'
								else: return 'True'
							else: return 'True'
						else: return 'True'
					else: return 'True'
				else: return 'True'
			elif obj[2]<=0:
				return 'True'
			else: return 'True'
		else: return 'False'
	else: return 'True'
