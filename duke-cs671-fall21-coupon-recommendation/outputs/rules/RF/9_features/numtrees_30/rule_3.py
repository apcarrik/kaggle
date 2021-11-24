def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Education, obj[4]: Occupation, obj[5]: Bar, obj[6]: Restaurant20to50, obj[7]: Direction_same, obj[8]: Distance
	# {"feature": "Restaurant20to50", "instances": 34, "metric_value": 0.9975, "depth": 1}
	if obj[6]>0.0:
		# {"feature": "Passanger", "instances": 24, "metric_value": 0.9799, "depth": 2}
		if obj[0]<=2:
			# {"feature": "Occupation", "instances": 19, "metric_value": 0.8997, "depth": 3}
			if obj[4]<=19:
				# {"feature": "Coupon", "instances": 17, "metric_value": 0.7871, "depth": 4}
				if obj[2]>0:
					# {"feature": "Time", "instances": 11, "metric_value": 0.4395, "depth": 5}
					if obj[1]<=3:
						return 'False'
					elif obj[1]>3:
						# {"feature": "Education", "instances": 2, "metric_value": 1.0, "depth": 6}
						if obj[3]<=1:
							return 'True'
						elif obj[3]>1:
							return 'False'
						else: return 'False'
					else: return 'True'
				elif obj[2]<=0:
					# {"feature": "Bar", "instances": 6, "metric_value": 1.0, "depth": 5}
					if obj[5]>0.0:
						return 'True'
					elif obj[5]<=0.0:
						return 'False'
					else: return 'False'
				else: return 'True'
			elif obj[4]>19:
				return 'True'
			else: return 'True'
		elif obj[0]>2:
			# {"feature": "Distance", "instances": 5, "metric_value": 0.7219, "depth": 3}
			if obj[8]>1:
				return 'True'
			elif obj[8]<=1:
				return 'False'
			else: return 'False'
		else: return 'True'
	elif obj[6]<=0.0:
		# {"feature": "Education", "instances": 10, "metric_value": 0.7219, "depth": 2}
		if obj[3]<=2:
			return 'True'
		elif obj[3]>2:
			# {"feature": "Occupation", "instances": 3, "metric_value": 0.9183, "depth": 3}
			if obj[4]<=6:
				return 'False'
			elif obj[4]>6:
				return 'True'
			else: return 'True'
		else: return 'False'
	else: return 'True'
