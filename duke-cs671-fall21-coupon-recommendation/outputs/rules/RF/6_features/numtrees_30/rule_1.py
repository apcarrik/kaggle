def findDecision(obj): #obj[0]: Passanger, obj[1]: Coupon, obj[2]: Education, obj[3]: Occupation, obj[4]: Restaurant20to50, obj[5]: Distance
	# {"feature": "Education", "instances": 34, "metric_value": 0.9975, "depth": 1}
	if obj[2]<=1:
		# {"feature": "Occupation", "instances": 19, "metric_value": 0.8997, "depth": 2}
		if obj[3]<=10:
			# {"feature": "Coupon", "instances": 12, "metric_value": 1.0, "depth": 3}
			if obj[1]>0:
				# {"feature": "Restaurant20to50", "instances": 9, "metric_value": 0.9183, "depth": 4}
				if obj[4]<=3.0:
					# {"feature": "Passanger", "instances": 8, "metric_value": 0.8113, "depth": 5}
					if obj[0]>0:
						# {"feature": "Distance", "instances": 7, "metric_value": 0.8631, "depth": 6}
						if obj[5]<=2:
							return 'True'
						elif obj[5]>2:
							return 'True'
						else: return 'True'
					elif obj[0]<=0:
						return 'True'
					else: return 'True'
				elif obj[4]>3.0:
					return 'False'
				else: return 'False'
			elif obj[1]<=0:
				return 'False'
			else: return 'False'
		elif obj[3]>10:
			return 'True'
		else: return 'True'
	elif obj[2]>1:
		# {"feature": "Passanger", "instances": 15, "metric_value": 0.9183, "depth": 2}
		if obj[0]<=2:
			return 'False'
		elif obj[0]>2:
			# {"feature": "Occupation", "instances": 7, "metric_value": 0.8631, "depth": 3}
			if obj[3]<=7:
				return 'True'
			elif obj[3]>7:
				# {"feature": "Coupon", "instances": 3, "metric_value": 0.9183, "depth": 4}
				if obj[1]>2:
					# {"feature": "Restaurant20to50", "instances": 2, "metric_value": 1.0, "depth": 5}
					if obj[4]>0.0:
						return 'True'
					elif obj[4]<=0.0:
						return 'False'
					else: return 'False'
				elif obj[1]<=2:
					return 'False'
				else: return 'False'
			else: return 'False'
		else: return 'True'
	else: return 'False'
