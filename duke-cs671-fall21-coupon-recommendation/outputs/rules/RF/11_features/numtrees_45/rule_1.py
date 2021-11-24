def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Age, obj[4]: Education, obj[5]: Occupation, obj[6]: Bar, obj[7]: Coffeehouse, obj[8]: Restaurant20to50, obj[9]: Direction_same, obj[10]: Distance
	# {"feature": "Time", "instances": 23, "metric_value": 0.9877, "depth": 1}
	if obj[1]>0:
		# {"feature": "Restaurant20to50", "instances": 17, "metric_value": 0.9975, "depth": 2}
		if obj[8]>0.0:
			# {"feature": "Distance", "instances": 15, "metric_value": 0.9968, "depth": 3}
			if obj[10]<=2:
				# {"feature": "Direction_same", "instances": 13, "metric_value": 0.9612, "depth": 4}
				if obj[9]<=0:
					# {"feature": "Coupon", "instances": 9, "metric_value": 0.7642, "depth": 5}
					if obj[2]>0:
						return 'True'
					elif obj[2]<=0:
						# {"feature": "Education", "instances": 3, "metric_value": 0.9183, "depth": 6}
						if obj[4]<=2:
							return 'False'
						elif obj[4]>2:
							return 'True'
						else: return 'True'
					else: return 'False'
				elif obj[9]>0:
					# {"feature": "Coupon", "instances": 4, "metric_value": 0.8113, "depth": 5}
					if obj[2]>0:
						return 'False'
					elif obj[2]<=0:
						return 'True'
					else: return 'True'
				else: return 'False'
			elif obj[10]>2:
				return 'False'
			else: return 'False'
		elif obj[8]<=0.0:
			return 'False'
		else: return 'False'
	elif obj[1]<=0:
		# {"feature": "Coupon", "instances": 6, "metric_value": 0.65, "depth": 2}
		if obj[2]<=2:
			return 'True'
		elif obj[2]>2:
			# {"feature": "Passanger", "instances": 2, "metric_value": 1.0, "depth": 3}
			if obj[0]>0:
				return 'False'
			elif obj[0]<=0:
				return 'True'
			else: return 'True'
		else: return 'False'
	else: return 'True'
