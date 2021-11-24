def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Education, obj[4]: Occupation, obj[5]: Bar, obj[6]: Restaurant20to50, obj[7]: Direction_same, obj[8]: Distance
	# {"feature": "Passanger", "instances": 23, "metric_value": 0.9656, "depth": 1}
	if obj[0]<=1:
		# {"feature": "Education", "instances": 13, "metric_value": 0.9957, "depth": 2}
		if obj[3]<=2:
			# {"feature": "Occupation", "instances": 10, "metric_value": 0.971, "depth": 3}
			if obj[4]>1:
				# {"feature": "Coupon", "instances": 9, "metric_value": 0.9183, "depth": 4}
				if obj[2]<=2:
					# {"feature": "Restaurant20to50", "instances": 5, "metric_value": 0.7219, "depth": 5}
					if obj[6]<=2.0:
						return 'True'
					elif obj[6]>2.0:
						# {"feature": "Bar", "instances": 2, "metric_value": 1.0, "depth": 6}
						if obj[5]>0.0:
							return 'False'
						elif obj[5]<=0.0:
							return 'True'
						else: return 'True'
					else: return 'False'
				elif obj[2]>2:
					# {"feature": "Distance", "instances": 4, "metric_value": 1.0, "depth": 5}
					if obj[8]<=1:
						return 'False'
					elif obj[8]>1:
						return 'True'
					else: return 'True'
				else: return 'False'
			elif obj[4]<=1:
				return 'False'
			else: return 'False'
		elif obj[3]>2:
			return 'False'
		else: return 'False'
	elif obj[0]>1:
		# {"feature": "Education", "instances": 10, "metric_value": 0.7219, "depth": 2}
		if obj[3]>0:
			return 'True'
		elif obj[3]<=0:
			# {"feature": "Occupation", "instances": 4, "metric_value": 1.0, "depth": 3}
			if obj[4]<=6:
				return 'False'
			elif obj[4]>6:
				return 'True'
			else: return 'True'
		else: return 'False'
	else: return 'True'
