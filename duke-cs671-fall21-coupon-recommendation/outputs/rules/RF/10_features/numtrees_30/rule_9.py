def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Education, obj[4]: Occupation, obj[5]: Bar, obj[6]: Coffeehouse, obj[7]: Restaurant20to50, obj[8]: Direction_same, obj[9]: Distance
	# {"feature": "Coupon", "instances": 34, "metric_value": 0.9774, "depth": 1}
	if obj[2]>2:
		# {"feature": "Education", "instances": 18, "metric_value": 0.9641, "depth": 2}
		if obj[3]<=1:
			# {"feature": "Distance", "instances": 9, "metric_value": 0.5033, "depth": 3}
			if obj[9]<=2:
				return 'True'
			elif obj[9]>2:
				return 'False'
			else: return 'False'
		elif obj[3]>1:
			# {"feature": "Bar", "instances": 9, "metric_value": 0.9183, "depth": 3}
			if obj[5]<=1.0:
				# {"feature": "Restaurant20to50", "instances": 6, "metric_value": 1.0, "depth": 4}
				if obj[7]<=1.0:
					# {"feature": "Passanger", "instances": 4, "metric_value": 0.8113, "depth": 5}
					if obj[0]>1:
						# {"feature": "Time", "instances": 2, "metric_value": 1.0, "depth": 6}
						if obj[1]>3:
							return 'True'
						elif obj[1]<=3:
							return 'False'
						else: return 'False'
					elif obj[0]<=1:
						return 'False'
					else: return 'False'
				elif obj[7]>1.0:
					return 'True'
				else: return 'True'
			elif obj[5]>1.0:
				return 'False'
			else: return 'False'
		else: return 'False'
	elif obj[2]<=2:
		# {"feature": "Occupation", "instances": 16, "metric_value": 0.6962, "depth": 2}
		if obj[4]<=6:
			# {"feature": "Passanger", "instances": 8, "metric_value": 0.9544, "depth": 3}
			if obj[0]<=1:
				# {"feature": "Education", "instances": 5, "metric_value": 0.971, "depth": 4}
				if obj[3]<=1:
					# {"feature": "Time", "instances": 3, "metric_value": 0.9183, "depth": 5}
					if obj[1]<=2:
						# {"feature": "Bar", "instances": 2, "metric_value": 1.0, "depth": 6}
						if obj[5]<=0.0:
							return 'False'
						elif obj[5]>0.0:
							return 'True'
						else: return 'True'
					elif obj[1]>2:
						return 'False'
					else: return 'False'
				elif obj[3]>1:
					return 'True'
				else: return 'True'
			elif obj[0]>1:
				return 'False'
			else: return 'False'
		elif obj[4]>6:
			return 'False'
		else: return 'False'
	else: return 'False'
