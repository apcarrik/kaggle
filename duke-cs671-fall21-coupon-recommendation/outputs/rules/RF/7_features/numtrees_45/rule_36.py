def findDecision(obj): #obj[0]: Passanger, obj[1]: Coupon, obj[2]: Education, obj[3]: Occupation, obj[4]: Restaurant20to50, obj[5]: Direction_same, obj[6]: Distance
	# {"feature": "Direction_same", "instances": 23, "metric_value": 0.9877, "depth": 1}
	if obj[5]<=0:
		# {"feature": "Occupation", "instances": 20, "metric_value": 1.0, "depth": 2}
		if obj[3]>4:
			# {"feature": "Coupon", "instances": 15, "metric_value": 0.971, "depth": 3}
			if obj[1]<=3:
				# {"feature": "Passanger", "instances": 11, "metric_value": 0.8454, "depth": 4}
				if obj[0]<=2:
					# {"feature": "Distance", "instances": 7, "metric_value": 0.5917, "depth": 5}
					if obj[6]>1:
						return 'False'
					elif obj[6]<=1:
						# {"feature": "Education", "instances": 2, "metric_value": 1.0, "depth": 6}
						if obj[2]<=0:
							return 'False'
						elif obj[2]>0:
							return 'True'
						else: return 'True'
					else: return 'False'
				elif obj[0]>2:
					# {"feature": "Distance", "instances": 4, "metric_value": 1.0, "depth": 5}
					if obj[6]>1:
						# {"feature": "Education", "instances": 3, "metric_value": 0.9183, "depth": 6}
						if obj[2]>0:
							# {"feature": "Restaurant20to50", "instances": 2, "metric_value": 1.0, "depth": 7}
							if obj[4]<=1.0:
								return 'False'
							else: return 'False'
						elif obj[2]<=0:
							return 'True'
						else: return 'True'
					elif obj[6]<=1:
						return 'False'
					else: return 'False'
				else: return 'False'
			elif obj[1]>3:
				# {"feature": "Distance", "instances": 4, "metric_value": 0.8113, "depth": 4}
				if obj[6]<=2:
					return 'True'
				elif obj[6]>2:
					return 'False'
				else: return 'False'
			else: return 'True'
		elif obj[3]<=4:
			# {"feature": "Coupon", "instances": 5, "metric_value": 0.7219, "depth": 3}
			if obj[1]<=3:
				return 'True'
			elif obj[1]>3:
				# {"feature": "Education", "instances": 2, "metric_value": 1.0, "depth": 4}
				if obj[2]>0:
					return 'False'
				elif obj[2]<=0:
					return 'True'
				else: return 'True'
			else: return 'False'
		else: return 'True'
	elif obj[5]>0:
		return 'True'
	else: return 'True'
