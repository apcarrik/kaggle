def findDecision(obj): #obj[0]: Passanger, obj[1]: Coupon, obj[2]: Education, obj[3]: Occupation, obj[4]: Restaurant20to50, obj[5]: Direction_same, obj[6]: Distance
	# {"feature": "Restaurant20to50", "instances": 85, "metric_value": 0.9555, "depth": 1}
	if obj[4]<=3.0:
		# {"feature": "Occupation", "instances": 82, "metric_value": 0.965, "depth": 2}
		if obj[3]>0:
			# {"feature": "Education", "instances": 81, "metric_value": 0.9599, "depth": 3}
			if obj[2]>1:
				# {"feature": "Coupon", "instances": 49, "metric_value": 0.9925, "depth": 4}
				if obj[1]<=2:
					# {"feature": "Passanger", "instances": 28, "metric_value": 0.9403, "depth": 5}
					if obj[0]>0:
						# {"feature": "Direction_same", "instances": 27, "metric_value": 0.951, "depth": 6}
						if obj[5]<=0:
							# {"feature": "Distance", "instances": 18, "metric_value": 0.9183, "depth": 7}
							if obj[6]<=2:
								return 'True'
							elif obj[6]>2:
								return 'True'
							else: return 'True'
						elif obj[5]>0:
							# {"feature": "Distance", "instances": 9, "metric_value": 0.9911, "depth": 7}
							if obj[6]<=1:
								return 'True'
							elif obj[6]>1:
								return 'False'
							else: return 'False'
						else: return 'True'
					elif obj[0]<=0:
						return 'True'
					else: return 'True'
				elif obj[1]>2:
					# {"feature": "Direction_same", "instances": 21, "metric_value": 0.9852, "depth": 5}
					if obj[5]<=0:
						# {"feature": "Distance", "instances": 16, "metric_value": 1.0, "depth": 6}
						if obj[6]<=2:
							# {"feature": "Passanger", "instances": 15, "metric_value": 0.9968, "depth": 7}
							if obj[0]>1:
								return 'False'
							elif obj[0]<=1:
								return 'True'
							else: return 'True'
						elif obj[6]>2:
							return 'False'
						else: return 'False'
					elif obj[5]>0:
						# {"feature": "Distance", "instances": 5, "metric_value": 0.7219, "depth": 6}
						if obj[6]<=1:
							# {"feature": "Passanger", "instances": 3, "metric_value": 0.9183, "depth": 7}
							if obj[0]<=1:
								return 'False'
							else: return 'False'
						elif obj[6]>1:
							return 'False'
						else: return 'False'
					else: return 'False'
				else: return 'False'
			elif obj[2]<=1:
				# {"feature": "Coupon", "instances": 32, "metric_value": 0.8571, "depth": 4}
				if obj[1]>1:
					# {"feature": "Passanger", "instances": 25, "metric_value": 0.7219, "depth": 5}
					if obj[0]<=1:
						# {"feature": "Distance", "instances": 17, "metric_value": 0.874, "depth": 6}
						if obj[6]<=2:
							# {"feature": "Direction_same", "instances": 15, "metric_value": 0.9183, "depth": 7}
							if obj[5]<=0:
								return 'True'
							elif obj[5]>0:
								return 'True'
							else: return 'True'
						elif obj[6]>2:
							return 'True'
						else: return 'True'
					elif obj[0]>1:
						return 'True'
					else: return 'True'
				elif obj[1]<=1:
					# {"feature": "Passanger", "instances": 7, "metric_value": 0.9852, "depth": 5}
					if obj[0]>0:
						# {"feature": "Distance", "instances": 6, "metric_value": 0.9183, "depth": 6}
						if obj[6]<=2:
							# {"feature": "Direction_same", "instances": 5, "metric_value": 0.971, "depth": 7}
							if obj[5]<=0:
								return 'False'
							else: return 'False'
						elif obj[6]>2:
							return 'False'
						else: return 'False'
					elif obj[0]<=0:
						return 'True'
					else: return 'True'
				else: return 'False'
			else: return 'True'
		elif obj[3]<=0:
			return 'False'
		else: return 'False'
	elif obj[4]>3.0:
		return 'True'
	else: return 'True'
