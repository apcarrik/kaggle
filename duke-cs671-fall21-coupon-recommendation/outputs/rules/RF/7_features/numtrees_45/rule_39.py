def findDecision(obj): #obj[0]: Passanger, obj[1]: Coupon, obj[2]: Education, obj[3]: Occupation, obj[4]: Restaurant20to50, obj[5]: Direction_same, obj[6]: Distance
	# {"feature": "Coupon", "instances": 23, "metric_value": 0.9877, "depth": 1}
	if obj[1]>0:
		# {"feature": "Education", "instances": 21, "metric_value": 0.9587, "depth": 2}
		if obj[2]<=2:
			# {"feature": "Distance", "instances": 16, "metric_value": 0.8113, "depth": 3}
			if obj[6]>1:
				# {"feature": "Restaurant20to50", "instances": 10, "metric_value": 0.971, "depth": 4}
				if obj[4]<=1.0:
					# {"feature": "Passanger", "instances": 8, "metric_value": 1.0, "depth": 5}
					if obj[0]<=1:
						# {"feature": "Occupation", "instances": 6, "metric_value": 0.9183, "depth": 6}
						if obj[3]>2:
							# {"feature": "Direction_same", "instances": 5, "metric_value": 0.971, "depth": 7}
							if obj[5]<=0:
								return 'True'
							elif obj[5]>0:
								return 'True'
							else: return 'True'
						elif obj[3]<=2:
							return 'True'
						else: return 'True'
					elif obj[0]>1:
						return 'False'
					else: return 'False'
				elif obj[4]>1.0:
					return 'True'
				else: return 'True'
			elif obj[6]<=1:
				return 'True'
			else: return 'True'
		elif obj[2]>2:
			# {"feature": "Occupation", "instances": 5, "metric_value": 0.7219, "depth": 3}
			if obj[3]<=9:
				return 'False'
			elif obj[3]>9:
				# {"feature": "Direction_same", "instances": 2, "metric_value": 1.0, "depth": 4}
				if obj[5]<=0:
					return 'True'
				elif obj[5]>0:
					return 'False'
				else: return 'False'
			else: return 'True'
		else: return 'False'
	elif obj[1]<=0:
		return 'False'
	else: return 'False'
