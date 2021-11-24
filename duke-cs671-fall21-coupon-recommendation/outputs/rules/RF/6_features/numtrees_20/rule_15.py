def findDecision(obj): #obj[0]: Passanger, obj[1]: Coupon, obj[2]: Education, obj[3]: Occupation, obj[4]: Restaurant20to50, obj[5]: Distance
	# {"feature": "Coupon", "instances": 51, "metric_value": 0.9931, "depth": 1}
	if obj[1]<=3:
		# {"feature": "Restaurant20to50", "instances": 29, "metric_value": 0.8936, "depth": 2}
		if obj[4]>0.0:
			# {"feature": "Passanger", "instances": 25, "metric_value": 0.9427, "depth": 3}
			if obj[0]>0:
				# {"feature": "Distance", "instances": 23, "metric_value": 0.8865, "depth": 4}
				if obj[5]<=2:
					# {"feature": "Education", "instances": 20, "metric_value": 0.9341, "depth": 5}
					if obj[2]<=3:
						# {"feature": "Occupation", "instances": 18, "metric_value": 0.9641, "depth": 6}
						if obj[3]<=15:
							return 'True'
						elif obj[3]>15:
							return 'False'
						else: return 'False'
					elif obj[2]>3:
						return 'True'
					else: return 'True'
				elif obj[5]>2:
					return 'True'
				else: return 'True'
			elif obj[0]<=0:
				return 'False'
			else: return 'False'
		elif obj[4]<=0.0:
			return 'True'
		else: return 'True'
	elif obj[1]>3:
		# {"feature": "Occupation", "instances": 22, "metric_value": 0.9457, "depth": 2}
		if obj[3]<=10:
			# {"feature": "Passanger", "instances": 14, "metric_value": 1.0, "depth": 3}
			if obj[0]>0:
				# {"feature": "Distance", "instances": 12, "metric_value": 0.9799, "depth": 4}
				if obj[5]<=1:
					# {"feature": "Education", "instances": 6, "metric_value": 0.65, "depth": 5}
					if obj[2]>0:
						return 'False'
					elif obj[2]<=0:
						# {"feature": "Restaurant20to50", "instances": 3, "metric_value": 0.9183, "depth": 6}
						if obj[4]>0.0:
							return 'False'
						elif obj[4]<=0.0:
							return 'False'
						else: return 'False'
					else: return 'False'
				elif obj[5]>1:
					# {"feature": "Restaurant20to50", "instances": 6, "metric_value": 0.9183, "depth": 5}
					if obj[4]<=1.0:
						# {"feature": "Education", "instances": 3, "metric_value": 0.9183, "depth": 6}
						if obj[2]<=2:
							return 'False'
						elif obj[2]>2:
							return 'True'
						else: return 'True'
					elif obj[4]>1.0:
						return 'True'
					else: return 'True'
				else: return 'True'
			elif obj[0]<=0:
				return 'True'
			else: return 'True'
		elif obj[3]>10:
			# {"feature": "Passanger", "instances": 8, "metric_value": 0.5436, "depth": 3}
			if obj[0]<=1:
				return 'False'
			elif obj[0]>1:
				# {"feature": "Education", "instances": 2, "metric_value": 1.0, "depth": 4}
				if obj[2]<=0:
					# {"feature": "Restaurant20to50", "instances": 2, "metric_value": 1.0, "depth": 5}
					if obj[4]<=1.0:
						# {"feature": "Distance", "instances": 2, "metric_value": 1.0, "depth": 6}
						if obj[5]<=2:
							return 'False'
						else: return 'False'
					else: return 'False'
				else: return 'False'
			else: return 'False'
		else: return 'False'
	else: return 'False'
