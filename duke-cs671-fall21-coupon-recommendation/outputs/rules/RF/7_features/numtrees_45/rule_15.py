def findDecision(obj): #obj[0]: Passanger, obj[1]: Coupon, obj[2]: Education, obj[3]: Occupation, obj[4]: Restaurant20to50, obj[5]: Direction_same, obj[6]: Distance
	# {"feature": "Education", "instances": 23, "metric_value": 0.8865, "depth": 1}
	if obj[2]<=2:
		# {"feature": "Occupation", "instances": 16, "metric_value": 0.6962, "depth": 2}
		if obj[3]<=8:
			# {"feature": "Coupon", "instances": 11, "metric_value": 0.4395, "depth": 3}
			if obj[1]<=2:
				return 'True'
			elif obj[1]>2:
				# {"feature": "Restaurant20to50", "instances": 4, "metric_value": 0.8113, "depth": 4}
				if obj[4]>1.0:
					return 'True'
				elif obj[4]<=1.0:
					# {"feature": "Passanger", "instances": 2, "metric_value": 1.0, "depth": 5}
					if obj[0]<=1:
						# {"feature": "Direction_same", "instances": 2, "metric_value": 1.0, "depth": 6}
						if obj[5]<=0:
							# {"feature": "Distance", "instances": 2, "metric_value": 1.0, "depth": 7}
							if obj[6]<=1:
								return 'False'
							else: return 'False'
						else: return 'False'
					else: return 'False'
				else: return 'False'
			else: return 'True'
		elif obj[3]>8:
			# {"feature": "Restaurant20to50", "instances": 5, "metric_value": 0.971, "depth": 3}
			if obj[4]<=0.0:
				# {"feature": "Passanger", "instances": 3, "metric_value": 0.9183, "depth": 4}
				if obj[0]<=1:
					return 'False'
				elif obj[0]>1:
					return 'True'
				else: return 'True'
			elif obj[4]>0.0:
				return 'True'
			else: return 'True'
		else: return 'True'
	elif obj[2]>2:
		# {"feature": "Coupon", "instances": 7, "metric_value": 0.9852, "depth": 2}
		if obj[1]<=3:
			# {"feature": "Occupation", "instances": 4, "metric_value": 0.8113, "depth": 3}
			if obj[3]<=6:
				# {"feature": "Passanger", "instances": 2, "metric_value": 1.0, "depth": 4}
				if obj[0]>0:
					return 'False'
				elif obj[0]<=0:
					return 'True'
				else: return 'True'
			elif obj[3]>6:
				return 'True'
			else: return 'True'
		elif obj[1]>3:
			return 'False'
		else: return 'False'
	else: return 'False'
