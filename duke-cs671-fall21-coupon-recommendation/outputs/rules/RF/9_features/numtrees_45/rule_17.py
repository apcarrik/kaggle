def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Education, obj[4]: Occupation, obj[5]: Bar, obj[6]: Restaurant20to50, obj[7]: Direction_same, obj[8]: Distance
	# {"feature": "Coupon", "instances": 23, "metric_value": 0.9321, "depth": 1}
	if obj[2]<=3:
		# {"feature": "Occupation", "instances": 12, "metric_value": 0.65, "depth": 2}
		if obj[4]>1:
			# {"feature": "Distance", "instances": 11, "metric_value": 0.4395, "depth": 3}
			if obj[8]<=2:
				return 'True'
			elif obj[8]>2:
				# {"feature": "Education", "instances": 3, "metric_value": 0.9183, "depth": 4}
				if obj[3]>2:
					# {"feature": "Bar", "instances": 2, "metric_value": 1.0, "depth": 5}
					if obj[5]>2.0:
						return 'True'
					elif obj[5]<=2.0:
						return 'False'
					else: return 'False'
				elif obj[3]<=2:
					return 'True'
				else: return 'True'
			else: return 'True'
		elif obj[4]<=1:
			return 'False'
		else: return 'False'
	elif obj[2]>3:
		# {"feature": "Bar", "instances": 11, "metric_value": 0.994, "depth": 2}
		if obj[5]<=1.0:
			# {"feature": "Passanger", "instances": 7, "metric_value": 0.8631, "depth": 3}
			if obj[0]<=1:
				# {"feature": "Education", "instances": 4, "metric_value": 1.0, "depth": 4}
				if obj[3]<=2:
					# {"feature": "Time", "instances": 3, "metric_value": 0.9183, "depth": 5}
					if obj[1]<=0:
						# {"feature": "Occupation", "instances": 2, "metric_value": 1.0, "depth": 6}
						if obj[4]<=5:
							return 'True'
						elif obj[4]>5:
							return 'False'
						else: return 'False'
					elif obj[1]>0:
						return 'False'
					else: return 'False'
				elif obj[3]>2:
					return 'True'
				else: return 'True'
			elif obj[0]>1:
				return 'True'
			else: return 'True'
		elif obj[5]>1.0:
			return 'False'
		else: return 'False'
	else: return 'False'
