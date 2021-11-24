def findDecision(obj): #obj[0]: Passanger, obj[1]: Coupon, obj[2]: Education, obj[3]: Occupation, obj[4]: Bar, obj[5]: Restaurant20to50, obj[6]: Direction_same, obj[7]: Distance
	# {"feature": "Restaurant20to50", "instances": 34, "metric_value": 0.9975, "depth": 1}
	if obj[5]<=2.0:
		# {"feature": "Coupon", "instances": 30, "metric_value": 0.971, "depth": 2}
		if obj[1]>1:
			# {"feature": "Passanger", "instances": 20, "metric_value": 0.9928, "depth": 3}
			if obj[0]<=2:
				# {"feature": "Occupation", "instances": 15, "metric_value": 0.971, "depth": 4}
				if obj[3]>2:
					# {"feature": "Bar", "instances": 12, "metric_value": 0.8113, "depth": 5}
					if obj[4]>0.0:
						# {"feature": "Education", "instances": 9, "metric_value": 0.5033, "depth": 6}
						if obj[2]<=3:
							return 'False'
						elif obj[2]>3:
							return 'True'
						else: return 'True'
					elif obj[4]<=0.0:
						# {"feature": "Education", "instances": 3, "metric_value": 0.9183, "depth": 6}
						if obj[2]>0:
							# {"feature": "Direction_same", "instances": 2, "metric_value": 1.0, "depth": 7}
							if obj[6]<=0:
								# {"feature": "Distance", "instances": 2, "metric_value": 1.0, "depth": 8}
								if obj[7]<=2:
									return 'True'
								else: return 'True'
							else: return 'True'
						elif obj[2]<=0:
							return 'True'
						else: return 'True'
					else: return 'True'
				elif obj[3]<=2:
					return 'True'
				else: return 'True'
			elif obj[0]>2:
				return 'True'
			else: return 'True'
		elif obj[1]<=1:
			# {"feature": "Passanger", "instances": 10, "metric_value": 0.469, "depth": 3}
			if obj[0]>0:
				return 'False'
			elif obj[0]<=0:
				return 'True'
			else: return 'True'
		else: return 'False'
	elif obj[5]>2.0:
		return 'True'
	else: return 'True'
