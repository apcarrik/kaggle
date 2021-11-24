def findDecision(obj): #obj[0]: Passanger, obj[1]: Coupon, obj[2]: Education, obj[3]: Occupation, obj[4]: Bar, obj[5]: Restaurant20to50, obj[6]: Direction_same, obj[7]: Distance
	# {"feature": "Education", "instances": 34, "metric_value": 0.9975, "depth": 1}
	if obj[2]<=2:
		# {"feature": "Occupation", "instances": 29, "metric_value": 0.9923, "depth": 2}
		if obj[3]>3:
			# {"feature": "Restaurant20to50", "instances": 23, "metric_value": 0.9877, "depth": 3}
			if obj[5]<=1.0:
				# {"feature": "Bar", "instances": 17, "metric_value": 0.9975, "depth": 4}
				if obj[4]<=1.0:
					# {"feature": "Coupon", "instances": 13, "metric_value": 0.9612, "depth": 5}
					if obj[1]>0:
						# {"feature": "Passanger", "instances": 10, "metric_value": 1.0, "depth": 6}
						if obj[0]>0:
							# {"feature": "Distance", "instances": 9, "metric_value": 0.9911, "depth": 7}
							if obj[7]>1:
								# {"feature": "Direction_same", "instances": 6, "metric_value": 1.0, "depth": 8}
								if obj[6]<=0:
									return 'False'
								else: return 'False'
							elif obj[7]<=1:
								# {"feature": "Direction_same", "instances": 3, "metric_value": 0.9183, "depth": 8}
								if obj[6]>0:
									return 'True'
								elif obj[6]<=0:
									return 'True'
								else: return 'True'
							else: return 'True'
						elif obj[0]<=0:
							return 'False'
						else: return 'False'
					elif obj[1]<=0:
						return 'False'
					else: return 'False'
				elif obj[4]>1.0:
					# {"feature": "Coupon", "instances": 4, "metric_value": 0.8113, "depth": 5}
					if obj[1]<=2:
						return 'True'
					elif obj[1]>2:
						return 'False'
					else: return 'False'
				else: return 'True'
			elif obj[5]>1.0:
				# {"feature": "Passanger", "instances": 6, "metric_value": 0.65, "depth": 4}
				if obj[0]<=2:
					return 'True'
				elif obj[0]>2:
					# {"feature": "Bar", "instances": 3, "metric_value": 0.9183, "depth": 5}
					if obj[4]<=0.0:
						return 'True'
					elif obj[4]>0.0:
						return 'False'
					else: return 'False'
				else: return 'True'
			else: return 'True'
		elif obj[3]<=3:
			return 'False'
		else: return 'False'
	elif obj[2]>2:
		return 'True'
	else: return 'True'
