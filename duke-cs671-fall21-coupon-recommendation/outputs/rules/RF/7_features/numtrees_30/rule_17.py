def findDecision(obj): #obj[0]: Passanger, obj[1]: Coupon, obj[2]: Education, obj[3]: Occupation, obj[4]: Restaurant20to50, obj[5]: Direction_same, obj[6]: Distance
	# {"feature": "Occupation", "instances": 34, "metric_value": 0.99, "depth": 1}
	if obj[3]<=9:
		# {"feature": "Coupon", "instances": 24, "metric_value": 0.9799, "depth": 2}
		if obj[1]<=3:
			# {"feature": "Restaurant20to50", "instances": 18, "metric_value": 1.0, "depth": 3}
			if obj[4]<=2.0:
				# {"feature": "Direction_same", "instances": 16, "metric_value": 0.9887, "depth": 4}
				if obj[5]<=0:
					# {"feature": "Passanger", "instances": 15, "metric_value": 0.971, "depth": 5}
					if obj[0]<=2:
						# {"feature": "Education", "instances": 8, "metric_value": 0.8113, "depth": 6}
						if obj[2]<=2:
							# {"feature": "Distance", "instances": 5, "metric_value": 0.971, "depth": 7}
							if obj[6]>1:
								return 'False'
							elif obj[6]<=1:
								return 'False'
							else: return 'False'
						elif obj[2]>2:
							return 'False'
						else: return 'False'
					elif obj[0]>2:
						# {"feature": "Education", "instances": 7, "metric_value": 0.9852, "depth": 6}
						if obj[2]<=2:
							# {"feature": "Distance", "instances": 6, "metric_value": 1.0, "depth": 7}
							if obj[6]>1:
								return 'False'
							elif obj[6]<=1:
								return 'True'
							else: return 'True'
						elif obj[2]>2:
							return 'True'
						else: return 'True'
					else: return 'True'
				elif obj[5]>0:
					return 'True'
				else: return 'True'
			elif obj[4]>2.0:
				return 'True'
			else: return 'True'
		elif obj[1]>3:
			# {"feature": "Education", "instances": 6, "metric_value": 0.65, "depth": 3}
			if obj[2]>0:
				return 'False'
			elif obj[2]<=0:
				return 'True'
			else: return 'True'
		else: return 'False'
	elif obj[3]>9:
		# {"feature": "Distance", "instances": 10, "metric_value": 0.469, "depth": 2}
		if obj[6]<=2:
			return 'True'
		elif obj[6]>2:
			return 'False'
		else: return 'False'
	else: return 'True'
