def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Education, obj[4]: Occupation, obj[5]: Bar, obj[6]: Restaurant20to50, obj[7]: Direction_same, obj[8]: Distance
	# {"feature": "Coupon", "instances": 51, "metric_value": 0.9183, "depth": 1}
	if obj[2]>0:
		# {"feature": "Distance", "instances": 43, "metric_value": 0.8204, "depth": 2}
		if obj[8]<=2:
			# {"feature": "Time", "instances": 38, "metric_value": 0.6892, "depth": 3}
			if obj[1]<=2:
				# {"feature": "Restaurant20to50", "instances": 25, "metric_value": 0.4022, "depth": 4}
				if obj[6]<=3.0:
					# {"feature": "Occupation", "instances": 24, "metric_value": 0.2499, "depth": 5}
					if obj[4]>1:
						return 'True'
					elif obj[4]<=1:
						# {"feature": "Passanger", "instances": 2, "metric_value": 1.0, "depth": 6}
						if obj[0]>1:
							return 'False'
						elif obj[0]<=1:
							return 'True'
						else: return 'True'
					else: return 'False'
				elif obj[6]>3.0:
					return 'False'
				else: return 'False'
			elif obj[1]>2:
				# {"feature": "Education", "instances": 13, "metric_value": 0.9612, "depth": 4}
				if obj[3]>0:
					# {"feature": "Occupation", "instances": 7, "metric_value": 0.9852, "depth": 5}
					if obj[4]>6:
						# {"feature": "Passanger", "instances": 5, "metric_value": 0.971, "depth": 6}
						if obj[0]<=1:
							# {"feature": "Bar", "instances": 4, "metric_value": 0.8113, "depth": 7}
							if obj[5]<=2.0:
								return 'True'
							elif obj[5]>2.0:
								return 'False'
							else: return 'False'
						elif obj[0]>1:
							return 'False'
						else: return 'False'
					elif obj[4]<=6:
						return 'False'
					else: return 'False'
				elif obj[3]<=0:
					# {"feature": "Passanger", "instances": 6, "metric_value": 0.65, "depth": 5}
					if obj[0]>2:
						return 'True'
					elif obj[0]<=2:
						# {"feature": "Occupation", "instances": 2, "metric_value": 1.0, "depth": 6}
						if obj[4]<=6:
							return 'False'
						elif obj[4]>6:
							return 'True'
						else: return 'True'
					else: return 'False'
				else: return 'True'
			else: return 'True'
		elif obj[8]>2:
			# {"feature": "Time", "instances": 5, "metric_value": 0.7219, "depth": 3}
			if obj[1]<=1:
				# {"feature": "Education", "instances": 3, "metric_value": 0.9183, "depth": 4}
				if obj[3]<=0:
					return 'False'
				elif obj[3]>0:
					return 'True'
				else: return 'True'
			elif obj[1]>1:
				return 'False'
			else: return 'False'
		else: return 'False'
	elif obj[2]<=0:
		# {"feature": "Bar", "instances": 8, "metric_value": 0.8113, "depth": 2}
		if obj[5]<=1.0:
			return 'False'
		elif obj[5]>1.0:
			return 'True'
		else: return 'True'
	else: return 'False'
