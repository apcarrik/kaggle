def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Education, obj[4]: Occupation, obj[5]: Bar, obj[6]: Restaurant20to50, obj[7]: Direction_same, obj[8]: Distance
	# {"feature": "Time", "instances": 23, "metric_value": 0.9877, "depth": 1}
	if obj[1]>0:
		# {"feature": "Distance", "instances": 20, "metric_value": 0.9341, "depth": 2}
		if obj[8]>1:
			# {"feature": "Coupon", "instances": 16, "metric_value": 0.8113, "depth": 3}
			if obj[2]<=3:
				# {"feature": "Bar", "instances": 11, "metric_value": 0.9457, "depth": 4}
				if obj[5]<=1.0:
					# {"feature": "Restaurant20to50", "instances": 8, "metric_value": 1.0, "depth": 5}
					if obj[6]<=1.0:
						# {"feature": "Passanger", "instances": 5, "metric_value": 0.7219, "depth": 6}
						if obj[0]<=1:
							return 'True'
						elif obj[0]>1:
							# {"feature": "Occupation", "instances": 2, "metric_value": 1.0, "depth": 7}
							if obj[4]>6:
								return 'True'
							elif obj[4]<=6:
								return 'False'
							else: return 'False'
						else: return 'True'
					elif obj[6]>1.0:
						return 'False'
					else: return 'False'
				elif obj[5]>1.0:
					return 'False'
				else: return 'False'
			elif obj[2]>3:
				return 'False'
			else: return 'False'
		elif obj[8]<=1:
			# {"feature": "Education", "instances": 4, "metric_value": 0.8113, "depth": 3}
			if obj[3]>0:
				return 'True'
			elif obj[3]<=0:
				return 'False'
			else: return 'False'
		else: return 'True'
	elif obj[1]<=0:
		return 'True'
	else: return 'True'
