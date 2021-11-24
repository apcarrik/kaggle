def findDecision(obj): #obj[0]: Passanger, obj[1]: Coupon, obj[2]: Education, obj[3]: Occupation, obj[4]: Restaurant20to50, obj[5]: Distance
	# {"feature": "Distance", "instances": 127, "metric_value": 0.9964, "depth": 1}
	if obj[5]<=2:
		# {"feature": "Education", "instances": 106, "metric_value": 0.9791, "depth": 2}
		if obj[2]<=3:
			# {"feature": "Coupon", "instances": 100, "metric_value": 0.9896, "depth": 3}
			if obj[1]<=3:
				# {"feature": "Passanger", "instances": 68, "metric_value": 0.9488, "depth": 4}
				if obj[0]>0:
					# {"feature": "Restaurant20to50", "instances": 65, "metric_value": 0.9233, "depth": 5}
					if obj[4]<=2.0:
						# {"feature": "Occupation", "instances": 60, "metric_value": 0.9007, "depth": 6}
						if obj[3]<=21:
							return 'True'
						elif obj[3]>21:
							return 'False'
						else: return 'False'
					elif obj[4]>2.0:
						# {"feature": "Occupation", "instances": 5, "metric_value": 0.971, "depth": 6}
						if obj[3]>1:
							return 'False'
						elif obj[3]<=1:
							return 'True'
						else: return 'True'
					else: return 'False'
				elif obj[0]<=0:
					return 'False'
				else: return 'False'
			elif obj[1]>3:
				# {"feature": "Restaurant20to50", "instances": 32, "metric_value": 0.9745, "depth": 4}
				if obj[4]<=2.0:
					# {"feature": "Occupation", "instances": 28, "metric_value": 0.9059, "depth": 5}
					if obj[3]>0:
						# {"feature": "Passanger", "instances": 27, "metric_value": 0.8767, "depth": 6}
						if obj[0]<=1:
							return 'False'
						elif obj[0]>1:
							return 'False'
						else: return 'False'
					elif obj[3]<=0:
						return 'True'
					else: return 'True'
				elif obj[4]>2.0:
					return 'True'
				else: return 'True'
			else: return 'False'
		elif obj[2]>3:
			return 'True'
		else: return 'True'
	elif obj[5]>2:
		# {"feature": "Education", "instances": 21, "metric_value": 0.8631, "depth": 2}
		if obj[2]<=2:
			# {"feature": "Occupation", "instances": 17, "metric_value": 0.6723, "depth": 3}
			if obj[3]<=7:
				# {"feature": "Restaurant20to50", "instances": 13, "metric_value": 0.7793, "depth": 4}
				if obj[4]<=2.0:
					# {"feature": "Coupon", "instances": 12, "metric_value": 0.65, "depth": 5}
					if obj[1]<=1:
						return 'False'
					elif obj[1]>1:
						# {"feature": "Passanger", "instances": 6, "metric_value": 0.9183, "depth": 6}
						if obj[0]<=1:
							return 'False'
						else: return 'False'
					else: return 'False'
				elif obj[4]>2.0:
					return 'True'
				else: return 'True'
			elif obj[3]>7:
				return 'False'
			else: return 'False'
		elif obj[2]>2:
			# {"feature": "Coupon", "instances": 4, "metric_value": 0.8113, "depth": 3}
			if obj[1]<=2:
				# {"feature": "Occupation", "instances": 2, "metric_value": 1.0, "depth": 4}
				if obj[3]>4:
					return 'False'
				elif obj[3]<=4:
					return 'True'
				else: return 'True'
			elif obj[1]>2:
				return 'True'
			else: return 'True'
		else: return 'True'
	else: return 'False'
