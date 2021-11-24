def findDecision(obj): #obj[0]: Passanger, obj[1]: Coupon, obj[2]: Education, obj[3]: Occupation, obj[4]: Bar, obj[5]: Restaurant20to50, obj[6]: Direction_same, obj[7]: Distance
	# {"feature": "Passanger", "instances": 51, "metric_value": 0.9662, "depth": 1}
	if obj[0]<=2:
		# {"feature": "Occupation", "instances": 39, "metric_value": 0.9995, "depth": 2}
		if obj[3]<=12:
			# {"feature": "Education", "instances": 36, "metric_value": 0.9978, "depth": 3}
			if obj[2]<=2:
				# {"feature": "Coupon", "instances": 28, "metric_value": 0.9666, "depth": 4}
				if obj[1]>1:
					# {"feature": "Bar", "instances": 16, "metric_value": 0.8113, "depth": 5}
					if obj[4]>-1.0:
						# {"feature": "Distance", "instances": 15, "metric_value": 0.7219, "depth": 6}
						if obj[7]<=2:
							# {"feature": "Restaurant20to50", "instances": 14, "metric_value": 0.5917, "depth": 7}
							if obj[5]>0.0:
								# {"feature": "Direction_same", "instances": 12, "metric_value": 0.65, "depth": 8}
								if obj[6]<=0:
									return 'True'
								elif obj[6]>0:
									return 'True'
								else: return 'True'
							elif obj[5]<=0.0:
								return 'True'
							else: return 'True'
						elif obj[7]>2:
							return 'False'
						else: return 'False'
					elif obj[4]<=-1.0:
						return 'False'
					else: return 'False'
				elif obj[1]<=1:
					# {"feature": "Restaurant20to50", "instances": 12, "metric_value": 0.9799, "depth": 5}
					if obj[5]>0.0:
						# {"feature": "Bar", "instances": 10, "metric_value": 1.0, "depth": 6}
						if obj[4]<=2.0:
							# {"feature": "Distance", "instances": 9, "metric_value": 0.9911, "depth": 7}
							if obj[7]>1:
								# {"feature": "Direction_same", "instances": 6, "metric_value": 0.9183, "depth": 8}
								if obj[6]<=0:
									return 'True'
								elif obj[6]>0:
									return 'True'
								else: return 'True'
							elif obj[7]<=1:
								# {"feature": "Direction_same", "instances": 3, "metric_value": 0.9183, "depth": 8}
								if obj[6]<=0:
									return 'False'
								else: return 'False'
							else: return 'False'
						elif obj[4]>2.0:
							return 'False'
						else: return 'False'
					elif obj[5]<=0.0:
						return 'False'
					else: return 'False'
				else: return 'False'
			elif obj[2]>2:
				# {"feature": "Distance", "instances": 8, "metric_value": 0.8113, "depth": 4}
				if obj[7]>1:
					return 'False'
				elif obj[7]<=1:
					# {"feature": "Coupon", "instances": 4, "metric_value": 1.0, "depth": 5}
					if obj[1]>0:
						# {"feature": "Restaurant20to50", "instances": 3, "metric_value": 0.9183, "depth": 6}
						if obj[5]<=1.0:
							# {"feature": "Bar", "instances": 2, "metric_value": 1.0, "depth": 7}
							if obj[4]<=1.0:
								# {"feature": "Direction_same", "instances": 2, "metric_value": 1.0, "depth": 8}
								if obj[6]<=1:
									return 'True'
								else: return 'True'
							else: return 'True'
						elif obj[5]>1.0:
							return 'False'
						else: return 'False'
					elif obj[1]<=0:
						return 'True'
					else: return 'True'
				else: return 'True'
			else: return 'False'
		elif obj[3]>12:
			return 'False'
		else: return 'False'
	elif obj[0]>2:
		return 'True'
	else: return 'True'
