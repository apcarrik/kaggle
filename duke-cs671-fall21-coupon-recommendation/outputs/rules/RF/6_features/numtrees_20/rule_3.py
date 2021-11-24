def findDecision(obj): #obj[0]: Passanger, obj[1]: Coupon, obj[2]: Education, obj[3]: Occupation, obj[4]: Restaurant20to50, obj[5]: Distance
	# {"feature": "Passanger", "instances": 51, "metric_value": 0.9997, "depth": 1}
	if obj[0]<=2:
		# {"feature": "Distance", "instances": 44, "metric_value": 0.9865, "depth": 2}
		if obj[5]>1:
			# {"feature": "Restaurant20to50", "instances": 24, "metric_value": 0.8709, "depth": 3}
			if obj[4]<=2.0:
				# {"feature": "Coupon", "instances": 20, "metric_value": 0.6098, "depth": 4}
				if obj[1]<=3:
					# {"feature": "Occupation", "instances": 15, "metric_value": 0.7219, "depth": 5}
					if obj[3]>5:
						# {"feature": "Education", "instances": 9, "metric_value": 0.5033, "depth": 6}
						if obj[2]<=0:
							return 'False'
						elif obj[2]>0:
							return 'False'
						else: return 'False'
					elif obj[3]<=5:
						# {"feature": "Education", "instances": 6, "metric_value": 0.9183, "depth": 6}
						if obj[2]>0:
							return 'False'
						elif obj[2]<=0:
							return 'False'
						else: return 'False'
					else: return 'False'
				elif obj[1]>3:
					return 'False'
				else: return 'False'
			elif obj[4]>2.0:
				return 'True'
			else: return 'True'
		elif obj[5]<=1:
			# {"feature": "Occupation", "instances": 20, "metric_value": 0.971, "depth": 3}
			if obj[3]>2:
				# {"feature": "Restaurant20to50", "instances": 17, "metric_value": 0.874, "depth": 4}
				if obj[4]<=2.0:
					# {"feature": "Coupon", "instances": 15, "metric_value": 0.7219, "depth": 5}
					if obj[1]<=3:
						# {"feature": "Education", "instances": 9, "metric_value": 0.5033, "depth": 6}
						if obj[2]<=2:
							return 'True'
						elif obj[2]>2:
							return 'True'
						else: return 'True'
					elif obj[1]>3:
						# {"feature": "Education", "instances": 6, "metric_value": 0.9183, "depth": 6}
						if obj[2]<=2:
							return 'True'
						elif obj[2]>2:
							return 'True'
						else: return 'True'
					else: return 'True'
				elif obj[4]>2.0:
					return 'False'
				else: return 'False'
			elif obj[3]<=2:
				return 'False'
			else: return 'False'
		else: return 'True'
	elif obj[0]>2:
		return 'True'
	else: return 'True'
