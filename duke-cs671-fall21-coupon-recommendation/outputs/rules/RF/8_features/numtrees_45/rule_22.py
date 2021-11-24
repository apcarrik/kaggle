def findDecision(obj): #obj[0]: Passanger, obj[1]: Coupon, obj[2]: Education, obj[3]: Occupation, obj[4]: Bar, obj[5]: Restaurant20to50, obj[6]: Direction_same, obj[7]: Distance
	# {"feature": "Coupon", "instances": 23, "metric_value": 0.9986, "depth": 1}
	if obj[1]<=3:
		# {"feature": "Occupation", "instances": 17, "metric_value": 0.9774, "depth": 2}
		if obj[3]<=6:
			# {"feature": "Passanger", "instances": 10, "metric_value": 0.7219, "depth": 3}
			if obj[0]>0:
				# {"feature": "Direction_same", "instances": 9, "metric_value": 0.5033, "depth": 4}
				if obj[6]<=0:
					return 'True'
				elif obj[6]>0:
					# {"feature": "Education", "instances": 2, "metric_value": 1.0, "depth": 5}
					if obj[2]>1:
						return 'False'
					elif obj[2]<=1:
						return 'True'
					else: return 'True'
				else: return 'False'
			elif obj[0]<=0:
				return 'False'
			else: return 'False'
		elif obj[3]>6:
			# {"feature": "Passanger", "instances": 7, "metric_value": 0.8631, "depth": 3}
			if obj[0]>1:
				# {"feature": "Bar", "instances": 5, "metric_value": 0.971, "depth": 4}
				if obj[4]>0.0:
					# {"feature": "Education", "instances": 3, "metric_value": 0.9183, "depth": 5}
					if obj[2]<=0:
						# {"feature": "Distance", "instances": 2, "metric_value": 1.0, "depth": 6}
						if obj[7]<=1:
							return 'True'
						elif obj[7]>1:
							return 'False'
						else: return 'False'
					elif obj[2]>0:
						return 'True'
					else: return 'True'
				elif obj[4]<=0.0:
					return 'False'
				else: return 'False'
			elif obj[0]<=1:
				return 'False'
			else: return 'False'
		else: return 'False'
	elif obj[1]>3:
		# {"feature": "Occupation", "instances": 6, "metric_value": 0.65, "depth": 2}
		if obj[3]<=9:
			return 'False'
		elif obj[3]>9:
			return 'True'
		else: return 'True'
	else: return 'False'
