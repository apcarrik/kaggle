def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Education, obj[4]: Occupation, obj[5]: Bar, obj[6]: Restaurant20to50, obj[7]: Direction_same, obj[8]: Distance
	# {"feature": "Coupon", "instances": 34, "metric_value": 1.0, "depth": 1}
	if obj[2]>2:
		# {"feature": "Restaurant20to50", "instances": 17, "metric_value": 0.7871, "depth": 2}
		if obj[6]>1.0:
			return 'True'
		elif obj[6]<=1.0:
			# {"feature": "Bar", "instances": 7, "metric_value": 0.9852, "depth": 3}
			if obj[5]<=0.0:
				# {"feature": "Distance", "instances": 4, "metric_value": 0.8113, "depth": 4}
				if obj[8]<=2:
					return 'True'
				elif obj[8]>2:
					return 'False'
				else: return 'False'
			elif obj[5]>0.0:
				return 'False'
			else: return 'False'
		else: return 'False'
	elif obj[2]<=2:
		# {"feature": "Education", "instances": 17, "metric_value": 0.7871, "depth": 2}
		if obj[3]<=2:
			# {"feature": "Time", "instances": 12, "metric_value": 0.9183, "depth": 3}
			if obj[1]>0:
				# {"feature": "Occupation", "instances": 10, "metric_value": 0.7219, "depth": 4}
				if obj[4]<=5:
					return 'False'
				elif obj[4]>5:
					# {"feature": "Passanger", "instances": 4, "metric_value": 1.0, "depth": 5}
					if obj[0]>1:
						# {"feature": "Bar", "instances": 3, "metric_value": 0.9183, "depth": 6}
						if obj[5]<=1.0:
							return 'False'
						elif obj[5]>1.0:
							return 'True'
						else: return 'True'
					elif obj[0]<=1:
						return 'True'
					else: return 'True'
				else: return 'True'
			elif obj[1]<=0:
				return 'True'
			else: return 'True'
		elif obj[3]>2:
			return 'False'
		else: return 'False'
	else: return 'False'
