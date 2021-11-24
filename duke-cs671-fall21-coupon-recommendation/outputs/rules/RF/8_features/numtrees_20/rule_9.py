def findDecision(obj): #obj[0]: Passanger, obj[1]: Coupon, obj[2]: Education, obj[3]: Occupation, obj[4]: Bar, obj[5]: Restaurant20to50, obj[6]: Direction_same, obj[7]: Distance
	# {"feature": "Restaurant20to50", "instances": 51, "metric_value": 0.9367, "depth": 1}
	if obj[5]<=2.0:
		# {"feature": "Coupon", "instances": 45, "metric_value": 0.971, "depth": 2}
		if obj[1]<=3:
			# {"feature": "Passanger", "instances": 31, "metric_value": 0.8691, "depth": 3}
			if obj[0]<=2:
				# {"feature": "Distance", "instances": 19, "metric_value": 0.9819, "depth": 4}
				if obj[7]<=1:
					# {"feature": "Occupation", "instances": 11, "metric_value": 0.684, "depth": 5}
					if obj[3]<=19:
						# {"feature": "Education", "instances": 10, "metric_value": 0.469, "depth": 6}
						if obj[2]<=2:
							return 'True'
						elif obj[2]>2:
							# {"feature": "Direction_same", "instances": 4, "metric_value": 0.8113, "depth": 7}
							if obj[6]>0:
								return 'True'
							elif obj[6]<=0:
								return 'False'
							else: return 'False'
						else: return 'True'
					elif obj[3]>19:
						return 'False'
					else: return 'False'
				elif obj[7]>1:
					# {"feature": "Education", "instances": 8, "metric_value": 0.8113, "depth": 5}
					if obj[2]<=2:
						# {"feature": "Occupation", "instances": 4, "metric_value": 1.0, "depth": 6}
						if obj[3]>1:
							# {"feature": "Bar", "instances": 3, "metric_value": 0.9183, "depth": 7}
							if obj[4]<=1.0:
								return 'True'
							elif obj[4]>1.0:
								return 'False'
							else: return 'False'
						elif obj[3]<=1:
							return 'False'
						else: return 'False'
					elif obj[2]>2:
						return 'False'
					else: return 'False'
				else: return 'False'
			elif obj[0]>2:
				# {"feature": "Education", "instances": 12, "metric_value": 0.4138, "depth": 4}
				if obj[2]>0:
					return 'True'
				elif obj[2]<=0:
					# {"feature": "Occupation", "instances": 4, "metric_value": 0.8113, "depth": 5}
					if obj[3]<=5:
						return 'True'
					elif obj[3]>5:
						# {"feature": "Bar", "instances": 2, "metric_value": 1.0, "depth": 6}
						if obj[4]<=0.0:
							return 'False'
						elif obj[4]>0.0:
							return 'True'
						else: return 'True'
					else: return 'False'
				else: return 'True'
			else: return 'True'
		elif obj[1]>3:
			# {"feature": "Occupation", "instances": 14, "metric_value": 0.9403, "depth": 3}
			if obj[3]<=10:
				# {"feature": "Bar", "instances": 9, "metric_value": 0.9911, "depth": 4}
				if obj[4]>0.0:
					# {"feature": "Education", "instances": 6, "metric_value": 0.65, "depth": 5}
					if obj[2]<=0:
						# {"feature": "Passanger", "instances": 3, "metric_value": 0.9183, "depth": 6}
						if obj[0]>0:
							# {"feature": "Direction_same", "instances": 2, "metric_value": 1.0, "depth": 7}
							if obj[6]<=0:
								# {"feature": "Distance", "instances": 2, "metric_value": 1.0, "depth": 8}
								if obj[7]<=1:
									return 'True'
								else: return 'True'
							else: return 'True'
						elif obj[0]<=0:
							return 'True'
						else: return 'True'
					elif obj[2]>0:
						return 'True'
					else: return 'True'
				elif obj[4]<=0.0:
					return 'False'
				else: return 'False'
			elif obj[3]>10:
				return 'False'
			else: return 'False'
		else: return 'False'
	elif obj[5]>2.0:
		return 'True'
	else: return 'True'
