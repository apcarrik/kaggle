def findDecision(obj): #obj[0]: Passanger, obj[1]: Coupon, obj[2]: Education, obj[3]: Occupation, obj[4]: Bar, obj[5]: Restaurant20to50, obj[6]: Direction_same, obj[7]: Distance
	# {"feature": "Coupon", "instances": 23, "metric_value": 0.9877, "depth": 1}
	if obj[1]>1:
		# {"feature": "Passanger", "instances": 19, "metric_value": 0.8997, "depth": 2}
		if obj[0]<=2:
			# {"feature": "Occupation", "instances": 14, "metric_value": 0.9852, "depth": 3}
			if obj[3]>0:
				# {"feature": "Restaurant20to50", "instances": 13, "metric_value": 0.9612, "depth": 4}
				if obj[5]<=2.0:
					# {"feature": "Education", "instances": 12, "metric_value": 0.9183, "depth": 5}
					if obj[2]<=2:
						# {"feature": "Bar", "instances": 9, "metric_value": 0.7642, "depth": 6}
						if obj[4]>0.0:
							return 'True'
						elif obj[4]<=0.0:
							# {"feature": "Direction_same", "instances": 4, "metric_value": 1.0, "depth": 7}
							if obj[6]<=0:
								# {"feature": "Distance", "instances": 4, "metric_value": 1.0, "depth": 8}
								if obj[7]<=1:
									return 'True'
								else: return 'True'
							else: return 'True'
						else: return 'True'
					elif obj[2]>2:
						# {"feature": "Bar", "instances": 3, "metric_value": 0.9183, "depth": 6}
						if obj[4]<=0.0:
							# {"feature": "Direction_same", "instances": 2, "metric_value": 1.0, "depth": 7}
							if obj[6]<=1:
								# {"feature": "Distance", "instances": 2, "metric_value": 1.0, "depth": 8}
								if obj[7]<=1:
									return 'True'
								else: return 'True'
							else: return 'True'
						elif obj[4]>0.0:
							return 'False'
						else: return 'False'
					else: return 'False'
				elif obj[5]>2.0:
					return 'False'
				else: return 'False'
			elif obj[3]<=0:
				return 'False'
			else: return 'False'
		elif obj[0]>2:
			return 'True'
		else: return 'True'
	elif obj[1]<=1:
		return 'False'
	else: return 'False'
