def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Education, obj[4]: Occupation, obj[5]: Bar, obj[6]: Restaurant20to50, obj[7]: Direction_same, obj[8]: Distance
	# {"feature": "Coupon", "instances": 34, "metric_value": 0.9774, "depth": 1}
	if obj[2]>0:
		# {"feature": "Occupation", "instances": 28, "metric_value": 0.9059, "depth": 2}
		if obj[4]>0:
			# {"feature": "Direction_same", "instances": 26, "metric_value": 0.8404, "depth": 3}
			if obj[7]<=0:
				# {"feature": "Education", "instances": 14, "metric_value": 0.3712, "depth": 4}
				if obj[3]<=2:
					return 'True'
				elif obj[3]>2:
					# {"feature": "Distance", "instances": 4, "metric_value": 0.8113, "depth": 5}
					if obj[8]<=1:
						return 'True'
					elif obj[8]>1:
						return 'False'
					else: return 'False'
				else: return 'True'
			elif obj[7]>0:
				# {"feature": "Restaurant20to50", "instances": 12, "metric_value": 1.0, "depth": 4}
				if obj[6]>0.0:
					# {"feature": "Time", "instances": 9, "metric_value": 0.9183, "depth": 5}
					if obj[1]>0:
						return 'False'
					elif obj[1]<=0:
						# {"feature": "Education", "instances": 4, "metric_value": 0.8113, "depth": 6}
						if obj[3]<=3:
							return 'True'
						elif obj[3]>3:
							return 'False'
						else: return 'False'
					else: return 'True'
				elif obj[6]<=0.0:
					return 'True'
				else: return 'True'
			else: return 'True'
		elif obj[4]<=0:
			return 'False'
		else: return 'False'
	elif obj[2]<=0:
		# {"feature": "Passanger", "instances": 6, "metric_value": 0.65, "depth": 2}
		if obj[0]>0:
			return 'False'
		elif obj[0]<=0:
			return 'True'
		else: return 'True'
	else: return 'False'
