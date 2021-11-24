def findDecision(obj): #obj[0]: Passanger, obj[1]: Coupon, obj[2]: Education, obj[3]: Occupation, obj[4]: Bar, obj[5]: Restaurant20to50, obj[6]: Direction_same, obj[7]: Distance
	# {"feature": "Passanger", "instances": 34, "metric_value": 0.99, "depth": 1}
	if obj[0]<=1:
		# {"feature": "Bar", "instances": 18, "metric_value": 0.9183, "depth": 2}
		if obj[4]<=2.0:
			# {"feature": "Coupon", "instances": 15, "metric_value": 0.7219, "depth": 3}
			if obj[1]<=2:
				# {"feature": "Education", "instances": 10, "metric_value": 0.8813, "depth": 4}
				if obj[2]>0:
					# {"feature": "Occupation", "instances": 7, "metric_value": 0.9852, "depth": 5}
					if obj[3]>1:
						# {"feature": "Distance", "instances": 5, "metric_value": 0.971, "depth": 6}
						if obj[7]<=2:
							# {"feature": "Restaurant20to50", "instances": 4, "metric_value": 0.8113, "depth": 7}
							if obj[5]>0.0:
								# {"feature": "Direction_same", "instances": 3, "metric_value": 0.9183, "depth": 8}
								if obj[6]<=0:
									return 'True'
								else: return 'True'
							elif obj[5]<=0.0:
								return 'True'
							else: return 'True'
						elif obj[7]>2:
							return 'False'
						else: return 'False'
					elif obj[3]<=1:
						return 'False'
					else: return 'False'
				elif obj[2]<=0:
					return 'False'
				else: return 'False'
			elif obj[1]>2:
				return 'False'
			else: return 'False'
		elif obj[4]>2.0:
			return 'True'
		else: return 'True'
	elif obj[0]>1:
		# {"feature": "Bar", "instances": 16, "metric_value": 0.6962, "depth": 2}
		if obj[4]<=3.0:
			# {"feature": "Restaurant20to50", "instances": 15, "metric_value": 0.5665, "depth": 3}
			if obj[5]<=1.0:
				# {"feature": "Coupon", "instances": 8, "metric_value": 0.8113, "depth": 4}
				if obj[1]>0:
					# {"feature": "Occupation", "instances": 7, "metric_value": 0.5917, "depth": 5}
					if obj[3]<=7:
						return 'True'
					elif obj[3]>7:
						return 'False'
					else: return 'False'
				elif obj[1]<=0:
					return 'False'
				else: return 'False'
			elif obj[5]>1.0:
				return 'True'
			else: return 'True'
		elif obj[4]>3.0:
			return 'False'
		else: return 'False'
	else: return 'True'
